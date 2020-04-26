import bs4
examplefile=open('example.html')
examplesoup= bs4.BeautifulSoup(examplefile,"html.parser")
taglist=examplesoup.select('#author')
print('taglist:',taglist)
print('taglist:',str(taglist))
print('dic:',taglist[0].attrs)
print('dic.value:',taglist[0].get('id'))
print('text:',taglist[0].getText())

