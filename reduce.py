# reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def add(x, y):
    return x+y


result = reduce(add, [1, 2, 3, 4, 5])
print(result)

print('--------分割线--------')


def fn(x, y):
    return x*10+y


print(reduce(fn, [1, 2, 3, 4, 5]))

# 如果考虑到str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print('--------分割线--------')
print(reduce(fn, map(char2num, '12345')))

# 整理称一个str2int的函数就是
print('--------分割线--------')
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x*10+y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('12345'))