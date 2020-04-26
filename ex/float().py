from functools import reduce
def str2float(s):
       s_int,s_float=s.split(".")
       #将s字符串以小数点为界，赋值给s_int和s_float两个部分
       
       return  int(s_int+s_float)/10**len(s_float)
       #两部分合并后转换为整型，再除以小数部位的位数
       #注：带有小数点的字符串不能转换为整型


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
