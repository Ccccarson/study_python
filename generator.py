# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的
# 而且，创建一个包含100多万个元素的列表，不仅占用了很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
# 所以，如果列表元素可以按照某种算法推算出来，可以在循环的过程中不断推算出后续的元素
# 这种一边循环一边计算的机制，称为生成器：generator

L=[x * x for x in range(10)]
print(L)

g=(x * x for x in range(10))
print(g)

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator

for n in g:
    print(n)

# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# 斐波拉契数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

print(fib(5))

# 要把 fib 函数变成一个generator,只需要把print(b)改成yield b就可以了
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

def fib1(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

print(fib1(5))

# generator和函数的执行路程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 把函数改成generator后，基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代

for n in fib1(5):
    print(n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值
# 如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration的value中
g=fib1(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
n=0
results=[]
for t in triangles():
    print(t)
    results.append(t)
    n=n+1
    if n==10:
        break
    