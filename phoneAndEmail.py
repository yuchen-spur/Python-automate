#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re
# TODO: Create telephone regex.
phoneRegex = re.compile (r'''(

    \d{4}                   # the first 4 mobilephone number or areaCode of landline
    (\s|-)?                 # separator
    \d{8}|\d{11}|\d{8}      # the 11 mobilephone number or 8 mainNunber
                            of landline or 8(total) no areaCode number(unfinished)


    )''',re.VERBOSE)


# TODO: Create email regex.
emailRegex = re.compile (r'''(
    (www\.)?
    [a-zA-Z0-9._%+-]+        # username       
    @                        # @ symbol
    [a-zA-Z0-9]+             # domain name
    (\.[a-zA-Z]{2,4})        # dot-anything
    

    )''',re.VERBOSE)


# TODO: Find matches in clipboard text.
message=(str(pyperclip.paste()))
matches=[]
for groups in phoneRegex.findall(message):
    matches.append(groups[0])
    
for groups in emailRegex.findall(message):
    matches.append(groups[0])

#message=('Hello, my number is 15251537482,0510-85736201,051085736201,85736201\
#         www.694215319@qq.com,694215319@qq.com,m15251537482@163.com')
#phoneRegex.findall(message)
#emailRegex.findall(message)


# TODO: Copy results to the clipboard.
if len(matches)!=0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('There\'s no number or email!')

input ('Please input any key to continue.')

