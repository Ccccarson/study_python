# 直接在class中定义属性，这种属性是类属性
class Student(object):
    name = 'Student'


# 当我们定义一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
s = Student()
print(s.name)
print(Student.name)
s.name = "Michael"
print(s.name)
print(Student.name)
del s.name
print(s.name)

#在编写程序时，千万不要对实例属性和类属性使用相同的名字，因为相同的名称的实例属性将屏蔽掉类属性
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性


class Students(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Students.count =Students.count+1


# print(Students.count)
bart = Students('Bart')
print(Students.count)
lisa = Students('Lisa')
print(Students.count)
