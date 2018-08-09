#! /usr/bin/evn pyton3

# 配合 getattr() setattr() hasattr() 我们可以直接操作一个对象的状态
class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=Myobject()

hasattr(obj,'x')
print(obj.x)
hasattr(obj,'y')

setattr(obj,'y',19)
hasattr(obj,'y')
getattr(obj,'y')
print(obj.y)

getattr(obj,'z')
# 可以传入一个default参数，如果属性不存在，就返回默认值
getattr(obj,'z',404)
# 也可以获得对象方法
getattr(obj,'power')