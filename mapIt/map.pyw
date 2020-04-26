#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import sys,webbrowser,logging,pyperclip

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s\
- %(message)s')

#https://map.baidu.com/search/上海理工大学新光电大楼/

import sys,webbrowser,logging
if  len(sys.argv)>1:
    # Get address from command line.
    address=''.join(sys.argv[1:])
    logging.info("get %s",address)
else:
    address=pyperclip.paste()
    # TODO: Get address from clipboard.
webbrowser.open('https://map.baidu.com/search/'+address)


