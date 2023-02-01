# pip install PyPdf2

from PyPDF2 import PdfFileReader

# Path to PDF file
pdf_file_name = 'sample.pdf'

# Open the file in binary mode for reading
with open(pdf_file_name, 'rb') as pdf_file:
    # Read the PDF file
    pdf_reader = PdfFileReader(pdf_file)
    # Get the number of pages in the PDF file
    pages_nums = pdf_reader.numPages
    # Iterate over each page number
    for page_num in range(pages_nums):
        # Read the give PDF file page
        page = pdf_reader.getPage(page_num)
        # Extract text from the given PDF page
        text = page.extractText()

        print(text)
