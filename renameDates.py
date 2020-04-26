#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.
# Cautious: NOT apply for filename with two dates.

import os,re,shutil
datapattern=re.compile(r'''
^([a-zA-Z]*?)                 # all text before data
((0|1|)?\d)-            # MM
((0|1|2|3)?\d)-        # DD
(19|20\d\d)            # YYYY
(.*?)$                 # all text after data

''',re.VERBOSE)

a=0

for filename in os.listdir('.'):
    if len(datapattern.findall(filename))!=0:
        k = datapattern.findall(filename) 

        for i in range(len(k)):
            print(k[i][0]+k[i][3]+'-'+k[i][1]+'-'+k[i][5]+k[i][6])
            a=1

            newname=k[i][0]+k[i][3]+'-'+k[i][1]+'-'+k[i][5]+k[i][6]
            absworkingdir=os.path.abspath('.')
            amerFilename=os.path.join(absworkingdir,filename)
            euroFilename=os.path.join(absworkingdir,newname)
            shutil.move(amerFilename, euroFilename)

            

if a!=1:
    print ('Not Found')


