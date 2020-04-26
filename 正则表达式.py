import re
def name_of_email(addr):
    m = re.match(r'^(<(\w*\s\w*)>\s\w*|\w*)\@\w*\.\w*$', addr)    
    print(m.group(1))
    return m.group(1)
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
