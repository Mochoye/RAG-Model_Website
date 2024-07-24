import pdfplumber
import sys
import os

if len(sys.argv) < 2:
    print("Usage: pdftomd.py <pdf_file_path>")
    sys.exit(1)

pdf_file = sys.argv[1]
print(pdf_file)
markdown_file = os.path.splitext(pdf_file)[0] + '.md'

with pdfplumber.open(pdf_file) as pdf:
    print("PDF TO Markdown working")
    markdown_text = ""
    for page in pdf.pages:
        markdown_text += page.extract_text()

with open(markdown_file, "w") as file:
    file.write(markdown_text)
