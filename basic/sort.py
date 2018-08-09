# sorted()函数可以对list进行排序
l=[36,5,-12,9,32]
print(sorted(l))
# 此外，sorted()函数也是一个高阶函数，它还可以接受一个key函数来实现自定义的排序
l=sorted([36,35,-12,9,-21],key=abs)
print(l)
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于‘Z’<‘a’，结果，大写字母Z回排在小写字母a的前面
# 给sorted函数传入key函数，即可实现忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，可以传入第三个参数reverse=True