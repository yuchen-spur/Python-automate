import traceback

try:
    raise Exception ('There is an error')
except:
    file=open('.\error.txt','w')
    file.write(traceback.format_exc())
    file.close()
    
    
