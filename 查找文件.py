import os, sys

print('输入查询的文件:')
doc_name=input()
top_dir=r'C:\Users\69421\Desktop\311'
#print('输入查找位置:')
#top_dir=input()
print('')

def find_doc(doc_name,top_dir):
    #怎么实现不输入，使用默认值，是要用关键字参数么
    a=0
    for dir_path,subpaths,files in os.walk(top_dir):
    #os.walk是generator,不是list; 生成的是tuple(路径，[文件夹列表]，[文件列表])
        for exist_name in files:

            if doc_name in exist_name:#in 表示非完全匹配
                print(exist_name)
                print(os.path.join(dir_path, exist_name))
                print('')
                a=1
    if a==0:
        print('没有找到相关文件!')
        print('')
        
find_doc(doc_name,top_dir)

input('Please any key to exit')


