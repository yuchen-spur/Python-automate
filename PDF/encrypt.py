import PyPDF2
pdfobj=open('meetingminutes.pdf','rb')
readobj=PyPDF2.PdfFileReader(pdfobj)
writeobj=PyPDF2.PdfFileWriter()

for pagenum in range(readobj.numPages):
    writeobj.addPage(readobj.getPage(pagenum))

writeobj.encrypt('swordfish')
result=open('encryptedminutes.pdf','wb')
writeobj.write(result)
result.close()
    
