import requests


res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

try:
    res.raise_for_status()
except Exception as err:
    print('There is an error:',err)

playfile=open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(10000):
    playfile.write(chunk)

playfile.close()
    


