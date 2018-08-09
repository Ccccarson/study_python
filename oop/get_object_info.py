#!/usr/bin/env python3
# 使用type()
# 基本类型都可以用type()判断
print(type(123))
print(type('str'))
print(type(None))
# 如果一个变量指向函数或者类，也可以用type()判断
print(type(abs))
# type()函数返回对应的Class类型

import types
print('type(\'abc\')==str?', type('abc') == str)

# 判断基本类型可以直接写int,str等


# 使用 isinstance()
# 我们要判断class的类型，可以使用isinstance()函数

class Animals(object):
    pass


class Dog(Animals):
    pass


class Husky(Dog):
    pass


a = Animals()
d=Dog()
h=Husky()

print(isinstance(h,Husky))
print(isinstance(h,Animals))
print(isinstance(d,Husky))

# 能用type()判断的基本类型也可以用isinstance()判断
# 并且还可以判断一个变量是否时某些类型中的一种
# 总是优先使用isinstance()判断类型，可以将制定类型及其子类“一网打尽”

# 使用dit()
# 如果要获得一个对象所有属性和方法，，可以使用dir()函数，它返回一个包含字符串的list
print(dir('ABc'))

# 类似__xxx__的属性和方法在python中都是有特殊用途的，比如l__len__方法返回长度
len('ABC')
'ABC'.__len__()