# 位置参数 默认参数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5))
print(power(5,2))

def add_end(l=None):
    if l is None:
        l=[]
    l.append('END')
    return l

# 定义默认参数要牢记一点：默认参数必须指向不变对象

# 可变参数
def calc(*numbers):
    sum=0
    for num in numbers:
        sum+=num*num
    return sum
nums=[1,2,3]
print(calc(*nums))
# 定义可变参数 在参数前加一个* 在函数内部，参数numbers接受到的是一个tuple
# 调用该函数时，可以传入任意个参数，包括0个参数
# *nums表示吧nums这个list的所有元素作为可变参数传进去


# 关键字参数 
# 允许传入0个或任意个含参数名的参数，这些关键字参数再函数内部自动组装为dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('name','age')
extra={'caty':'shanghai','job':'web'}
person('carson',28,**extra)

# 命名关键字参数
# 和关键字参数**kw不同，命名关键参数需要一个特殊的分隔符*，*后面的参数被视为命名关键字参数
# 如果函数定义中已经有了一个可变参数，后面跟着 的命名关键字参数就不再需要一个特殊分隔符*
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# 命名关键字参数可以有缺省值
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分割符
# 如果缺少*，python解释器将无法识别位置参数和命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)
person2('Jack', 24, city='Beijing', job='Engineer')



# 参数组合
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 但是，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 比如：
def f1(a,b,c=0,*args,**kw):
    print(a,.b,c,args,kw)
def f2(a,b,c=0,*,d,**kw):
    print(a,v,c,d,kw)
# 所以对于任意函数，都可以通过类似fungc(*args,**kw)的形式调用它，无论它的参数是如何定义的
# 虽然可以组合多大5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差