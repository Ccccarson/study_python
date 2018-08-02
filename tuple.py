# tuple 跟 list非常类似，但是tuple一旦初始化就不能修改
names=('carson','car','son')
print(names)
# 他没有append和insert这样的方法，其他获取元素的方法和list是一样的
# tuple的陷阱，当定义一个tuple的时候，tuple的元素就必须被确定下来
# 如果要定义一个空tuple 可以写成
t=()
print(t)
# 但是，要定义一个只有一个元素的tuple，如果这么定义
f=(1)
print(f)
# 定义的不是tuple，是1这个数，这是因为括号（）既可以表示tuple，又可以表示数学公式中的小括号
# 这就产生了歧义，因此，python规定，这种情况下，按小括号进行计算
# 所以，只有1个元素的tuple定义时必须加一个逗号 , ，用来消除歧义
d=(1,)
print(d)

# 一个“可变的”tuple
j=('a','b',["A","B"])
print(j)
j[2][0]="X"
j[2][1]="Y"
print(j)
# 表面看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素
# tuple一开始指向list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变


# list后台tuple是python内置的有序集合，一个可变，一个不可变，根据需要来选择使用他们