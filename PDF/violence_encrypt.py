import PyPDF2
txtfile=open('dictionary.txt','r')
code=[]
for line in txtfile.readlines():
    code.append(line.rstrip())
    code.append(line.rstrip().lower())

pdffile=open('encryptedminutes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdffile)
for i in range(len(code)):
    if pdfReader.decrypt(code[i]):
        print(code[i])
        break

txtfile.close()
pdffile.close()
