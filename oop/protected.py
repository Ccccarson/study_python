# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在python中，实例的变量名如果以__开头
# 就变成了一个私有变量（private），只有内部可以访问，外部不能访问


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 供外部代码获取name和score
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 允许外部代码修改score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
# print(bart.__name)

print(bart.get_name())
print(bart.get_score())

bart.set_score(100)
print(bart.get_score())