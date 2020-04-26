import os, sys
import pprint

file=input('输入查询的文件:')
top_dir=r'C:\Users\69421\Desktop\python'

for roots,dirs,files in os.walk(top_dir):
    for filename in files:
        if file in filename:
            print(os.path.join(roots,filename))
            totalroot=os.path.join(roots,filename)

fileopen=open(totalroot)
pprint.pprint(fileopen.readlines())
    

