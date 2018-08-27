# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


print(Student('Carson'))

# __str__()返回用户看到的字符串 __repr__()返回程序开发者看到的字符串，也就是__repr__()是为调试服务的

# __iter__
# 如果一个类想被用于for..in循环，类似list或者tuple哪样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，知道遇到StopIteration错误时退出循环


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)

# __getitem__


class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a
f=Fib1()
f[10]
list(range(100))[5:10]
# 对于fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断

class Fib2(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
f1=Fib2()
f1[0:5]