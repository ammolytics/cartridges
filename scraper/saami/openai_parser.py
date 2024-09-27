from openai import OpenAI

import os
import logging
import json
import re

logger = logging.getLogger(__name__)

class OpenAIParser: 
    def __init__(self): 
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def parse_with_retries(self, pdf_file, tries):
        # Sometimes the AI is lazy and doesn't do a good job.
        # So we have to beg it nicely to try again.
        json_response = None
        while json_response == None and tries > 0:
            tries -= 1

            json_response = self.parse(pdf_file)
            if json_response != None:
                # We got a response, let's see how good it is.
                # Name always seems to be extracted, but not the numbers for some reason.
                # If we are at the end of our tries we just settle for what we have.
                if "diameter_in" in json_response or tries <= 0:
                    return json_response
                    break
                else:
                    # Let's wipe this and try again.
                    json_response = None
                    
        return None



    def parse(self, file_path):
        client = self.client

        logger.info("Parsing %s with OpenAI", file_path)

        vector_store = client.beta.vector_stores.create(
            name="SAAMI specs",
        )

        with open(file_path, 'rb') as f:
            client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id,
                files=[f]
            )

        assistant = client.beta.assistants.create(
            name="SAAMI pdf parser",
            instructions=(
                "You are a reader and interpeter of SAAMI catridge specification pdf files."
                "Never add any other text to the response."
            ),
            tools=[{"type": "file_search"}],
            tool_resources={
            "file_search": {
                "vector_store_ids": [vector_store.id]
            }
            },
            model="gpt-3.5-turbo",
        )

        thread = client.beta.threads.create()

        prompt = f"""
        The attached PDF contains a SAAMI cartridge and chamber specification document.
        Please provide the following information in JSON format:
        1. The name of the cartridge. Use the JSON key "name".
        3. The maximum overall length of the cartridge in inches. Use the JSON key "coal_max_in".
        4. The maximum overall length of the cartridge in mm. Use the JSON key "coal_max_mm".
        5. The caliber of the bullet in inches. Use the JSON key "diameter_in".
        6. The caliber of the bullet in mm. Use the JSON key "diameter_mm".

        Respond only with a JSON object.
        """

        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt,
        )

        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )

        result = ""

        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)

            for message in messages:
                if message.role != "assistant":
                    continue

                assert message.content[0].type == "text"
                result = message.content[0].text.value

            client.beta.assistants.delete(assistant.id)

        if result == "":
            return None

        return self.reformat(result)

    # The json format we receive from open ai is kept as simple as possible.
    # Reformat this into what the repo standard is.
    def reformat(self, json_str):
        # These seem to come through sometimes but not always
        json_str = json_str.replace("```json", "")
        json_str = json_str.replace("```", "")
        # Sometimes a stray \" shows up
        json_str = json_str.replace("\\\"", "")
        
        print(json_str)
        parsed_json = json.loads(json_str)
        
        # Sanity checks
        if "name" not in parsed_json:
            return None
        
        result = {
            "name": parsed_json["name"],
            "specs": {},
            "standard": "SAAMI",
        }
        
        # Everything else we treat as optional
        if "coal_max_in" in parsed_json and self.is_valid(parsed_json["coal_max_in"]):
            result["specs"]["coal_in"] = parsed_json["coal_max_in"]

        if "coal_max_mm" in parsed_json and self.is_valid(parsed_json["coal_max_mm"]):
            result["specs"]["coal_mm"] = parsed_json["coal_max_mm"]
                        
        if "diameter_in" in parsed_json and self.is_valid(parsed_json["diameter_in"]):
            result["diameter_in"] = parsed_json["diameter_in"]

        if "diameter_mm" in parsed_json and self.is_valid(parsed_json["diameter_mm"]):
            result["diameter_mm"] = parsed_json["diameter_mm"]
        
        return result
    
    def is_valid(self, str):
        if not str:
            return False
        
        if str == "N/A":
            return False
        
        if str == "NA":
            return False

        if str == "--":
            return False
        
        if str == "Not provided":
            return False
        
        return True
    
    def cleanup_data(self, data):
        if "coal_in" in data["specs"]:
            data["specs"]["coal_in"] = self.cleanup_number(data["specs"]["coal_in"])
            
        if "coal_mm" in data["specs"]:
            data["specs"]["coal_mm"] = self.cleanup_number(data["specs"]["coal_mm"])

        if "diameter_in" in data:
            data["diameter_in"] = self.cleanup_number(data["diameter_in"])

        if "diameter_mm" in data:
            data["diameter_mm"] = self.cleanup_number(data["diameter_mm"])
            
        return data
    
    def cleanup_number(self, field):
        # Sometimes these strings contain stray "inches" or "mm". Strip that
        if isinstance(field, str):
            field = re.sub("[^0-9\.]", "", field)
            return float(field)
        
        return field