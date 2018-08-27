class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(99)
s.get_score()
s.set_score(999)

# Python内置的@property装饰器负责把一个方法编程属性调用


class Student1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# 把一个getter方法编程属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器 @score.setter,负责把一个setter方法变成属性赋值
# 于是，我们就有了一个可控的属性操作
s1 = Student1()
s1.score = 60
s1.score
s1.score = 999

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性


class Student2(object):
    @property
    def brith(self):
        return self._brith

    @brith.setattr
    def brith(self, value):
        self._brith = value

    @property
    def age(self):
        return 2018-self._brith

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
# 这样，程序运行时就减少了出错的可能性
