import PyPDF2
pdfobj=open('meetingminutes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfobj)
page=pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter=PyPDF2.PdfFileWriter()#在python中创建空pdf
pdfWriter.addPage(page)#对Writer对象添加Page对象
resultpdffile=open('rotatePage.pdf','wb')
pdfWriter.write(resultpdffile)
#向 Writer对象 的 write()方法传入一个 File对象
resultpdffile.close()
pdfobj.close()
