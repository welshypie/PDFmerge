from PyPDF2 import PdfFileMerger

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