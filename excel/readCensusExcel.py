#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl,pprint

print('Opening workbook...')
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb['Population by Census Tract']
countydata={}

# TODO: Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2,sheet.max_row+1):
    # Read data
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value

    #set default in dic
    countydata.setdefault(state,{})
    countydata[state].setdefault(county,{'tracts':0,'pop':0})#need to set twice

    #calculate tracts and pop   
    countydata[state][county]['tracts']+=1
    countydata[state][county]['pop']+=int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
file=open('census2010.py','w')
file.write('All_data='+pprint.pformat(countydata))
file.close()

print('Done')


    
