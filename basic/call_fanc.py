# python内置了很多有用得函数，我们可以直接调用，例如

# abs()求绝对值
x = abs(100)
y = abs(-20)
print(x, y)

# max()求最大值
print('max(1, 2, 3) =', max(1, 2, 3))

# min()求最小值
print('min(1, 2, 3) =', min(1, 2, 3))

# sum() 求和函数
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

# 数据类型得转换

# int()把其他数据类型转为整数
print(int('123'))
print(int(12.34))

# float()用于将整数和字符串转成浮点数
print(float(12.34))
print(float('12.34'))

# str()把其他数据类型转成字符串
print(str('123'))

# bool()把其他数据类型转成布尔值
print(bool(1))
print(bool(''))