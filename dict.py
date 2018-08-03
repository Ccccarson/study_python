# python内置了字典：dict的支持，dict全称dictionary，在其他语言里称为map
# 使用键-值(key-value)存储，具有极快的查找速度
d={'carson':27,'shazi':25}
print(d['carson'])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['car']=7
print(d['car'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
# 如果key不存在，dict就会报错
# 要避免key不存在报错，有两种方法
# 一种是通过in判断key是否存在
print('son' in d)
# 二是通过dict提供的get()方法，如果key不存在，可以返回none，或者自己指定的value
print(d.get('son'))
print(d.get('son',-1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('car')
print(d)

# 和list相比 dict有以下几个特点
# 1.查找和插入的速度极快，不会随着key的增加而变慢
# 2.需要占用大量的内存，内存浪费多
# 而list相反：
# 1.查找和插入的时间随着元素的增加而增加
# 2.占用空间小，浪费内存少

# dict可以用在需要告诉茶皂的很多地方，在python代码中几户无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）