import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))
#lambda 的作用是把class转换成dict,dict才能转换成json对象（字符串格式）
