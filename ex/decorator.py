def sayName(func):
    #def inner():
       print("I'm Yu")
        #return func()
       return func

@sayName
def sayHi():
    print('Hello, World')

sayHi()
