#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os,zipfile

#os.chdir(r'C:\Users\69421\Desktop')
def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder=os.path.abspath(folder)
    # Make sure path is abs.

    # Figure out the filename this code should use based on
    # what files already exist.
    number=1
    while True:
        namefile = os.path.basename(folder)+'_'+str(number)+'.rar'
        if not os.path.exists(namefile):
            break
        number = number+1

    # Create the ZIP file.
    print('Creating %s...'%(namefile))
    backupZip = zipfile.ZipFile(namefile,'w')

    for root,dirs,filenames in os.walk(folder):#os.walk() return is 'C:\...\...'
        print('Adding files in %s'%(root))
        #Add all dirs.
        backupZip.write(os.path.relpath(root))

        for filename in filenames:
            if filename.startswith(os.path.basename(folder)+'_') \
               and filename.endswith('.rar'):
                continue
            #Add all files.
            backupZip.write(os.path.join(os.path.relpath(root),filename))

    print('Done')
    backupZip.close()

backupToZip(r'C:\Users\69421\Desktop\python')








            
