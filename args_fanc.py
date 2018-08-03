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


# 关键字参数 允许传入0个或任意个含参数名的参数，这些关键字参数再函数内部自动组装为dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'othner:',kw)