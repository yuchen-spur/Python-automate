class Screen(object):
    
    @property
    def width(self):         #这个函数就是self.width
        return self._width   #一定要加_,不然陷入死循环
    @width.setter            # width=width.setter(width)??
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    
    @property
    def resolution(self):
        return self.width*self.height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
