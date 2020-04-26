import PyPDF2
pdffileobj=open('meetingminutes.pdf','rb')#二进制
pdfReader=PyPDF2.PdfFileReader(pdffileobj)
num =pdfReader.numPages#页数
pageobj=pdfReader.getPage(0)
page1_word=pageobj.extractText()#第一页上的文字
#print(page1_word)
########################################
pdffileobj2=open('encrypted.pdf','rb')
pdfReader2=PyPDF2.PdfFileReader(pdffileobj2)
if_encryptedpdf=pdfReader2.isEncrypted#是否加密
print(if_encryptedpdf)
TorF=pdfReader2.decrypt('rosebud')#输入口令,正确1，错误0
pageobj2=pdfReader2.getPage(0)
newpage_word=pageobj2.extractText()
#print(newpage_word)
########################################


