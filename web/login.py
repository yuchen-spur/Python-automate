from selenium import webdriver


browser = webdriver.Edge()

# browser.get('https://passport.bilibili.com/login')
browser.get('https://www.bilibili.com')
linkElem = browser.find_element_by_class_name('logout-face')
# '登录'not be found,here used left image,its name 'logout-face'
linkElem.click()

windows = browser.window_handles
browser.switch_to.window(windows[-1])
# switch window 1 to 2

nameElm = browser.find_element_by_id('login-username')
nameElm.send_keys('15251537482')
passwordElm = browser.find_element_by_id('login-passwd')
passwordElm.send_keys('951753')

