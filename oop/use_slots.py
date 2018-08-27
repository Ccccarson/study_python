# 正常情况下，当我们定义了一个class，创建一个class实例后，我们可以给该实例绑定任何属性和方法
class Student(object):
    pass

s=Student()
s.name='Carson'
print(s.name)

def set_age(self,age):# 定义一个函数作为实例方法
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
s.age

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2=Student() # 创建新的实例
s2.set_age(25) # 尝试调用方法

# 为了给所有的实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score=score
Student.set_score=set_score

s.set_score(100)
s.score

# 使用__slots__
# 为了达到限制的目的，python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该实例能添加的属性
class Student1(object):
    __slots__=('name','age') # 用tuple定义允许绑定的属性名称

s3=Student1() # 创建心的实例
s3.name="Carson" # 绑定属性name
s3.age=25 # 绑定属性age
s3.score=99 # 绑定属性score
# 由于score没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类时不起作用的