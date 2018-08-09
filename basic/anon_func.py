print(list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# 用匿名函数有个好处，因为匿名函数没有名字，不必担心函数名会冲突
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数


f = lambda x: x * x


print(f)

# 同样，也可以把匿名函数作为返回值返回


def built(x, y):
    return lambda: x*x+y*y


def is_odd(n):
    s=lambda n: n % 2 == 1
    return s(n)

L=list(filter(is_odd,range(1,20)))
print(L)