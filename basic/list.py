names=['carson','car','son']
# 读取列表（类似于平时用到的array）
print(names[0])
# 列表追加元素
names.append('carson_1')
print(names)
# 把元素添加到指定位置
names.insert(1,'car_1')
print(names)
# 删除末尾元素
names.pop()
print(names)
# 删除制定位置的元素
names.pop(1)
print(names)
# 替换指定位置的元素
names[2]=28
print(names)
# 获取list长度
print(len(names))