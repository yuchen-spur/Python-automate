from PIL import Image

row=6
col=4

catIm=Image.open('zophie.png')
faceIm=catIm.crop((335,345,565,560))#cut off the cat head
facewidth,faceheight=faceIm.size#measure the head size
cat_cat=Image.new('RGBA',(col*facewidth,row*faceheight))#create the appropriate png

for left in range(0,col*facewidth,facewidth):
    for top in range(0,row*faceheight,faceheight):
        print(left,top)
        cat_cat.paste(faceIm,(left,top))

cat_cat.save('tiled.png')
