import csv
examplefile=open('example.csv','r')
examplereader=csv.reader(examplefile)
#list(examplereader)法一
for row in examplereader:#法二
    print(str(examplereader.line_num)+str(row))
    
examplefile.close()

examplefile=open('example.csv','a',newline='')#否则一行隔一行
examplewriter=csv.writer(examplefile)
examplewriter.writerow(['Hello,world','eggs','bacon','ham'])
examplewriter.writerow(['spam','eggs','bacon','ham'])

examplefile.close()
