import PyPDF3, os

os.chdir('C:\\users\\rahul.goyal\\documents')

pdf1File = open('RBI-GradeB-Prep.pdf', 'rb')
pdf2File = open('Leave Policy ION India.pdf', 'rb')

reader1 = PyPDF3.PdfFileReader(pdf1File)
reader2 = PyPDF3.PdfFileReader(pdf2File)
writer = PyPDF3.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outFile = open('Comb_Doc.pdf', 'wb')
writer.write(outFile)
outFile.close()
pdf2File.close()
pdf1File.close()