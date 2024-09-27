import os
import tempfile
import logging

from pypdf import PdfWriter, PdfReader

logger = logging.getLogger(__name__)

def split(pdf_file, first_page, last_page):  
    logger.info("Splitting " + pdf_file)

    inputpdf = PdfReader(open(pdf_file, "rb"))

    outputfiles = []

    for page in range(first_page, last_page):
        output = PdfWriter()
        output.add_page(inputpdf.pages[page])

        outputfile = "page%s.pdf" % page
        with open(outputfile, "wb") as outputStream:
            output.write(outputStream)

        outputfiles.append(outputfile)
    
    logger.info("Splitting done: %d files", len(outputfiles))

    return outputfiles
