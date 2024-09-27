import logging
import requests

logger = logging.getLogger(__name__)

class SaamiSource: 
    # Currently only one pdf so hard coding everything here
    def __init__(self): 
        self.url = "https://saami.org/wp-content/uploads/2023/11/ANSI-SAAMI-Z299.4-CFR-Approved-2015-12-14-Posting-Copy.pdf"
        self.page_start = 48
        self.page_end = 166

    def download(self, output_file):
        logger.info("Downloading " + self.url)
        response = requests.get(self.url)
        output_file.write(response.content)
        logger.info("Download done")