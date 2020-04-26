def trim(s):
       if  s=='':
              return s
       if (s[0]!=' ') and (s[-1]!=' '):
              return s
       if s[0]==' ':
              s=s[1:]
              return trim(s)

       else:
              s=s[0:-1]
              return trim(s)




if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
