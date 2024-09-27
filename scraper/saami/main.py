from source import SaamiSource
from openai_parser import OpenAIParser
from splitter import split

import os
import tempfile
import logging
import json

logging.basicConfig(encoding='utf-8', level=logging.INFO)

src = SaamiSource()
parser = OpenAIParser()

with tempfile.NamedTemporaryFile() as download_file:
    src.download(download_file)

    # Cut it into one file per caliber to make it easier on the AI
    split_pdf_files = split(
        download_file.name,
        src.page_start,
        src.page_end
    )

    # Send off to openai for parsing
    for pdf_file in split_pdf_files:
        # Skip if already found, we are probably resuming a job.
        json_file = pdf_file + ".json"
        if os.path.isfile(json_file):
            os.remove(pdf_file)
            continue

        json_response = parser.parse_with_retries(pdf_file, 2)
        # TODO there is probably a better way to tell the AI what exact format we want this in.
        # But I don't trust it so I'm just going to do some manual conversion here.
        json_response = parser.cleanup_data(json_response)

        with open(json_file, "wb") as stream:
            stream.write(json.dumps(json_response).encode())
            stream.write("\n".encode())

        os.remove(pdf_file)

