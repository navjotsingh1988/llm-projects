import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(filepath):
    file_content = ""
    # Open the PDF File
    reader = PdfReader(filepath)

    for page in reader.pages:
        # Get text from the page
        page_content = page.extract_text()
        if page_content:
            file_content += page_content + '\n'

    return file_content
