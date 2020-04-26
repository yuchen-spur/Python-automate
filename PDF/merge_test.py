import PyPDF2
pdf1obj=open('meetingminutes.pdf','rb')
pdf2obj=open('meetingminutes2.pdf','rb')
pdf1Reader=PyPDF2.PdfFileReader(pdf1obj)
pdf2Reader=PyPDF2.PdfFileReader(pdf2obj)
pdfWriter=PyPDF2.PdfFileWriter()#在python中创建一个空白PDF

#录入pdf1
for pageNum in range(pdf1Reader.numPages):
    pageobj=pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageobj)#把page对象给Writer对象

#录入pdf2
for pageNum in range(pdf2Reader.numPages):
    pageobj=pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageobj)

pdfoutputFile = open('combineminutes.pdf','wb')#在文件夹中创建实体
pdfWriter.write(pdfoutputFile)
pdfoutputFile.close()
pdf1obj.close()
pdf2obj.close()
