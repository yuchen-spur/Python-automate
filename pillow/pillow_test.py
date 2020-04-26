from PIL import ImageColor,Image
RGB_red=ImageColor.getcolor('red','RGBA')

catIm=Image.open('zophie.png')
width    = catIm.size[0]
height   = catIm.size[1]
name     = catIm.filename
Imformat = catIm.format
catIm.save('zophie.jpg')

im=Image.new('RGBA',(100,200),'CornflowerBlue')
im.save('cornflowerBlue.png')
im2=Image.new('RGBA',(20,20))#默认不可见的黑色
im2.save('transparentImage.png')

faceIm=catIm.crop((335,345,565,560))
faceIm.save('cropped.png')#裁剪

catCopyIm=catIm.copy()
catCopyIm.paste(faceIm,(0,0))
catCopyIm.paste(faceIm,(400,500))
catCopyIm.save('pasted.png')
facewidth,faceheight=faceIm.size#粘贴

quartersizedIm=catIm.resize((int(width/2),int(height/2)))
quartersizedIm.save('quartersizedIm.png')#调整大小

catIm.rotate(20).save('rotated20.png')#旋转

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
#镜像



