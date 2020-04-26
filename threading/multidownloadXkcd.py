#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests,os,bs4,threading
os.makedirs('xkcd',exist_ok=True)

def downloadXkcd(start,end):
    for urlnum in range(start,end):
        #download page
        print('download page http://xkcd.com/%s'%(urlnum))
        res=requests.get('http://xkcd.com/%s'%(urlnum))
        res.raise_for_status()

        soup=bs4.BeautifulSoup(res.text,"html.parser")

        #find the url of the comic image
        comicElem=soup.select('#comic img')
        if comicElem==[]:
            print('could not find comic image')
        else:
            comicUrl='http:'+comicElem[0].get('src')
            #download image
            print('downloading image %s...'%(comicUrl))
            res=requests.get(comicUrl)
            res.raise_for_status()

            #save the image
            imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
#downloadXkcd(1,99)
#create threading obj
downloadThreads=[]

for i in range(0,1400,100):
    downloadThread=threading.Thread(target=downloadXkcd,
                                    args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()#子线程给主线程加塞子，全部完成才能全部拔掉，让主线程继续
print('Done')#属于主线程



    
