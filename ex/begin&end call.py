
def log(text=''):

        #使用一个默认参数,实现有无‘execute’都可以执行

        def decorator(func):
        
                def wrapper(*args, **kw):

                        print ('%s end call: %s' %(text,func.__name__))

                        c = func(*args, **kw)

                        print ('%s begin call: %s' %(text,func.__name__))

                        return c

                        #now没有返回值，所以c是一个None,不会被执行

                return wrapper

        return decorator

#@log
@log('execute')

def now():

	print ('2019-11-11')

 

now()
