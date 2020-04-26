import pyautogui,time
width,height=pyautogui.size()

'''
for i in range(10):
    pyautogui.moveTo(100,100,duration=1)
    pyautogui.moveTo(500,100,duration=1)
    pyautogui.moveTo(500,500,duration=1)
    pyautogui.moveTo(100,500,duration=1)
'''

x_position,y_position=pyautogui.position()

'''
time.sleep(5)
pyautogui.scroll(500)#向上滚动
'''
'''
im=pyautogui.screenshot()
color=im.getpixel((50,200))
IFclick=pyautogui.pixelMatchesColor(50,200,(255,255,255))
#与预期的位置是否一致

left,top,width,height = pyautogui.locateOnScreen('submit.png')
#是屏幕上首次发现该图像时左边的x 坐标、顶边的 y 坐标、宽度以及高度。
center=pyautogui.center((left,top,width,height))
#返回中心坐标
pyautogui.click(center)
#点击识别到的图像
pyautogui.typewrite('Hello world!',0.3)
#在文本框中输入
pyautogui.typewrite(['left'])
#左移
'''
pyautogui.hotkey('ctrl', 'a')
#全选
