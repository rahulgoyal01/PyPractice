import PyPDF3
import os

os.chdir('C:\\Users\\rahul.goyal\\Documents')
pdfFile = open('Leave Policy ION India.pdf', 'rb')
reader = PyPDF3.PdfFileReader(pdfFile)
numPage = reader.numPages
print('No. of Pages in the PDF are : %s' % numPage)
page = reader.getPage(0)
print(page.extractText())


