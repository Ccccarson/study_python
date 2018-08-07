# slice 切片 
l=list(range(100))
print(l)
print(l[0:10])
print(l[-10:])

# l[0:10] 表示从索引 0 开始取，知道索引 10 为止，但不包括索引 10
# 如果第一个索引事 0 ，还可以省略
# 甚至什么都不写，只写 [:] 就可以原样复制一个list或者tuple
# 字符串‘xxx’也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果认识字符串

print('ABCDEFG'[:3])

def trim(l):
    if l[:1]==' ':
        return trim(l[1:len(l)])
    elif l[-1:]==' ':
        return trim(l[:len(l)-1])
    else:
        return '|'+l+'|'
print(trim('  hello  world  '))