# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但是循环的逻辑不如递归清晰
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会建议层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，回导致栈溢出
# 解决递归调用栈溢出的方法是通过 尾递归 优化，事实上尾递归和循环的效果是一样的
# 所以，把循环看成是一种特殊的尾递归函数也是可以的

# 尾递归是指，在函数返回的时候，盗用自身本身，并且，return语句不能包含表达式
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return 1
    return fact_iter(num-1,num*product)

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出

# 练习 汉诺塔
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4,'A','B','C')