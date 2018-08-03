# 在python中，定义一个函数要使用 def 语句，一次写出函数名、括号、货好种的参数和冒号
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
print(my_abs(-99))

def fibonacci(x):
    if x==0:
        return 0
    if x<=2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
print(fibonacci(5))

# 请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕并将结果返回。
# 因此内部通过条件判断和循环可以实现非常复杂的逻辑
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为none
# return None可以简写为return

# 如果想要定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass

# 参数检查 修改一下my_abs的定义
# 数据类型检查可以用内置函数isinstance()实现
def my_abs1(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x


# 返回多个值
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数
print(move(100,100,60,math.pi/6))


# 练习 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

# ax2 + bx + c = 0

# 的两个解。

def quadratic(a,b,c):
    if a==0:
        return "a is not 0"
    else:
        my_discriminant=b*b-4*a*c
        x1=(-b-math.sqrt(my_discriminant))/(2*a)
        x2=(-b+math.sqrt(my_discriminant))/(2*a)
        return x1,x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
