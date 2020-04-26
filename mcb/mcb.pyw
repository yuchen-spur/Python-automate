#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:  mcb save <keyword>    - Save clipboard to keyword.
#         mcb del <keyword>     - Delete keyword from list.
#         mcb <keyword>         - Loads keyword to clipboard.
#         mcb list              - Loads all keywords to clipboard.
#         mcb clear             - Clear all keywords in clipboard.



import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# TODO: Save clipboard content.
if len(sys.argv)==3:
    if sys.argv[1].lower()=='save':
        mcbShelf[sys.argv[2]]=pyperclip.paste()
    elif sys.argv[1].lower()=='del':
        mcbShelf.pop(sys.argv[2])
    
# TODO: List keywords and load content.
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower()=='clear':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
     
mcbShelf.close()
