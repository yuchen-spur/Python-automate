import re

message='Call me at 0510-15251537482 tomorrow. Landline number is 0510-85736201'

regex = re.compile(r'(\d\d\d\d)-(\d{11})|(\d\d\d\d)-(\d{8})')
mo=regex.findall(message)



print('areaCode is '+mo[0][0])
print('mainNumber is '+mo[0][1])

print('areaCode is '+mo[1][2])
print('mainNumber is '+mo[1][3])
