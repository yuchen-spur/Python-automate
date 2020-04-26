import os

print(os.getcwd())
os.chdir('C:\\Users\\69421\\Desktop\\python')
print(os.getcwd())
print(os.path.isabs(os.getcwd()))

print(os.path.dirname('C:\\Users\\69421\\Desktop\\python'))
print(os.path.basename('C:\\Users\\69421\\Desktop\\python'))

dirtuple=os.path.split('C:\\Users\\69421\\Desktop\\python')
#os方法分割-返回tuple
dirlist='C:\\Users\\69421\\Desktop\\python'.split(os.path.sep)
#char方法分割-返回list-完全分割
print(dirtuple)
print(dirlist)
print(os.path.join(dirtuple[0],dirtuple[1]))

print(os.path.getsize('C:\\Users\\69421\\Desktop\\python'))
print(os.listdir('C:\\Users\\69421\\Desktop\\python'))
totalsize=0

for filename in os.listdir('C:\\Users\\69421\\Desktop\\python'):
    totalsize=totalsize+os.path.getsize(os.path.join('C:\\Users\\69421\\Desktop\
\\python',filename))
print(totalsize)
#计算文件大小
