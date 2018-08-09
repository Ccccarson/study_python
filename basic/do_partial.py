# python的functools模块提供了很多有用的功能，其中一个就是偏函数(Partial function)
# int()函数可以把字符串转为整数，当仅传入字符串时，int()函数默认按十进制转换
print(int('123'))

# 但int()函数还提供额外的base参数。默认值是10，如果传入base参数，就可以做n进制的转换
print(int('12345', base=8))
print(int('12345', base=16))


def int2(x, base=2):
    return int(x, base)


# functools.partial就是帮助我们创建一个偏函数的
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))


# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住，返回一个新函数
