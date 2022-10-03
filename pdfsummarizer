import pdfplumber

with pdfplumber.open(r'testdoc3.pdf') as pdf:
  extracted_page = pdf.pages[23]
  extracted_text = extracted_page.extract_text()
  print(extracted_text)
