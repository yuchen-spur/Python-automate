#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.
import os,csv
os.makedirs('headerRemoved',exist_ok=True)
os.chdir('./removeCsvHeader')

# Loop through every file in the current working directory.
for csvfile in os.listdir('.'):
    if not csvfile.endswith('.csv'):
        continue
    print('Removing header from ' + csvfile + '...')

    # Read the CSV file in (skipping first row).
    csvfileobj=open(csvfile)
    csvReader=csv.reader(csvfileobj)
    data=[]
    for row in csvReader:#这里的row是list不是int
        if csvReader.line_num!=1:
            data.append(row)
    csvfileobj.close()

    # Write out the CSV file.
    csvfileobj=open(os.path.join('../headerRemoved',csvfile)\
                    ,'w',newline='')
    csvWriter=csv.writer(csvfileobj)
    for row in data:
        csvWriter.writerow(row)
    csvfileobj.close()
