# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
# 任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'carson'

# 以上就是python模块的标准文件模版

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()


# 第一行和第二行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

# 导入sys模块后，我们就又了变量sys指向该模块，利用sys这个变量。就可以访问sys模块的所有功能
# sys模块有一个argv变量，用list存储了命令行的所有参数，argv至少有一个元素，因为第一个参数永远是该 .py 文件的名称

# 作用域
# 正常的函数和变量名是公开的（public），可以直接被引用
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return "Hi, %s" % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 我们再模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法