# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数


def now():
    print('2018-08-09')


f = now
f()

# 函数对象又一个__name__属性，可以拿到函数的名字
print(f.__name__)

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)
# 本质上，decorator就是一个返回函数的高阶函数


def log(func):
    def wrapper(*arge, **kw):
        print('call %s():' % func.__name__)
        return func(*arge, **kw)
    return wrapper


@log
def now2():
    return print('2018-08-09')


now2()

print(now2.__name__)
# 把@log放到now2()函数的定义处，相当于执行了语句
# now2=log(now2)
# 由于log()是一个decorator,返回一个函数，所以，原来的now2()函数仍然存在，
# 只是现在同名的now2变量指向了一个新的函数，于是调用now2()将执行新函数
# 即在log()函数中返回的wrapper()函数
# wrapper()函数的参数定义是(*args,**kw),因此，wrapper()函数可以接受任意参数的调用
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数

# 经过decorator装饰之后的函数。它的__name__已经从原来的‘now2’变成了‘wrapper’
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些以来函数签名的代码执行就会出错
# 内置的functools.wraps

import functools

def log2(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

