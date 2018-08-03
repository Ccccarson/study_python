age=16
if age>18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')


age1=5
if age1>18:
    print('adult')
elif age1>=6:
    print('teenager')
else:
    print('kid')

# input 搭配 判断语句使用
# int()函数把str转换成整数
brith=int(input('brith:'))
if brith<2000:
    print('00前')
else:
    print('00后')