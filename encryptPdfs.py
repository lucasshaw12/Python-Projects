#! python3
# Go through and find every PDF in wording directory
# Save as {filename_encrypted.pdf}

import os, PyPDF2
from pathlib import Path

# Find all PDF files
pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

# Encrypt all PDF files
for file in pdfFiles:
	pdf = open(file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(file)
	pdfWriter = PyPDF2.PdfFileWriter()

	for pageNum in range(pdfReader.numPages):
		pdfWriter.addPage(pdfReader.getPage(pageNum))

	# get the stem name of each PDF file
	p = Path(file) 
	pdfStem = p.stem

	pdfWriter.encrypt('password')
	encryptedPdf = open(pdfStem + '_encrypted.pdf', 'wb')
	pdfWriter.write(encryptedPdf)
	encryptedPdf.close()
