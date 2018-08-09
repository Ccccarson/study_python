# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax+n
        return ax
    return sum


f = lazy_sum(1, 2, 3, 4, 5)
print(f)
print(f())
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包(Closure)”的程序结构拥有极大的威力
# 当我们调用lazy_sum时，每次调用都会返回一个新的函数，即使传入相同的参数

# 闭包


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
# 返回结果全部都是9，原因在于返回的函数引用了变量i，但它并非立即执行
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变


def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f4, f5, f6 = count2()
print(f4())
print(f5())
print(f6())
