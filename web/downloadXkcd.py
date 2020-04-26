#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url='http://xkcd.com'
# set download dirs
os.makedirs('xkcd',exist_ok=True)

# download html and image
while not url.endswith('#'):
    try:
        print('Downloading page %s...' % url)
        res=requests.get(url,timeout=10) # 10s-timeout
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,"html.parser")
        comicElem=soup.select('#comic img')
    except requests.exceptions.RequestException as e:
        print(e)
        continue # 10s-renew

    # there's no image in this url    
    if comicElem==[]: 
        print('No picture.')
    else :
        # get only-image url
        comicUrl='http:'+str(comicElem[0].get('src'))
        res=requests.get(comicUrl)
        res.raise_for_status()
        print('Downloading image %s...' % (comicUrl))
        picFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')

        #download image
        for chunk in res.iter_content(10000):
            picFile.write(chunk)
        picFile.close()

        #get the pre-image
        pre=soup.select('a[rel="prev"]')[0]
        url='http://xkcd.com'+pre.get('href')
        
