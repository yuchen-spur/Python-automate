#! python3
# quickWeather.py - Prints the weather for a location
# from the command line.
# 绝对路径上要保证命名文件夹的合法

import json,requests,sys

# Compute location from command line arguments.
if len(sys.argv)>=2:#the first is pyname
    location=' '.join(sys.argv[1:])#remove the first parament
else:
    print('输入要查询天气的城市：')
    location=input()

# Download the JSON data from OpenWeatherMap.org's API.
url='http://wthrcdn.etouch.cn/weather_mini?city=%s'%(location)
response=requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherdata=json.loads(response.text)

# Print weather descriptions.
w=weatherdata['data']['forecast']
print('%s最近的天气:\n' % (location))
for date in range(len(w)):
    print('日期：'+w[date]['date'])
    print('风力:'+w[date]['fengli'])
    print('风向:'+w[date]['fengxiang'])
    print('温度:'+w[date]['high']+' '+w[date]['low'])
    print('天气:'+w[date]['type'])
    print('')
