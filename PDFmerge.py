from PyPDF2 import PdfFileMerger
import os
import re

usrInput = ''
pdfs = []
while usrInput != '*':
	usrInput = input('Enter the filename in the local directory or enter * to finish: ')
	if usrInput != '*':
		pdfs.append(usrInput)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("output.pdf")
merger.close()


def list_pdfs():
	'''
	This function should return a list all PDFs in the current directory.
	'''
	dircontents = os.listdir(os.getcwd())
	pdflist = []
	for i in dircontents:
		if i[-4:] == ".pdf":
			pdflist.append(i)
			
	return pdflist