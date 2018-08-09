# 列表生成即List Comprehensions,是python内置的非常简单却强大的可以用来创建list的生成式

list1=list(range(1,11))
print(list1)

L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
# 列表生成式可以用一行语句代替循环生成上面的list
print([x * x for x in range(1,11)])
# 把要生成的元素 x * x 放到前面，后面跟for循环，就可以吧list创建出来

# for循环后面还可以加上if判断
print([x * x for x in range(1,11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列
print([m + n for m in  'ABC' for n in 'XYZ'])

# for 循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
# 因此，列表生成式也可以使用两个变量来生成list
d={'x':'A','y':'B','Z':'C'}
print([k + '=' + v for k,v in d.items()])

# 把list中所有的字符串变成小写
L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])
