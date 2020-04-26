#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

size = 300
logofilename = 'catlogo.png'

logoIm=Image.open(logofilename)
logoIm=logoIm.resize((70,66))
logowidth,logoheight = logoIm.size

os.makedirs('withlogo',exist_ok=True)

#Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg'))\
            or filename == logofilename:
        continue
    im = Image.open(filename)

    # Check if image needs to be resized.
    imwidth,imheight = im.size
    if (imwidth>300 or imheight>300):
        print('Resizing %s...'%(filename))
        if imwidth>=imheight:
            print('width>height')
            imheight=int(300*imheight/imwidth)
            imwidth=300
            im=im.resize((imwidth,imheight))
        else :
            print('width<height')
            imwidth=int(300*imwidth/imheight)
            imheight=300
            im=im.resize((imwidth,imheight))

    # TODO: Add the logo.
    left=imwidth-logowidth
    top=imheight-logoheight
    print('Adding logo to %s...'%(filename))
    im.paste(logoIm,(left,top),logoIm)#第三个参数让周围变透明
    im.save(os.path.join('withlogo',filename))
    
    
    
    
