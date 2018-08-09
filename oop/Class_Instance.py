# 面向对象最重要的概念就是类（Class）和实例（Instance），类是抽象的模版
# 而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同
# 定义类是通过 class 关键字


class Students(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return "B"
        else:
            return "C"
# class 后面紧接着类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类


# 定义好了Students类，就可以根据SStudents类创建处Students实例，创建实例是通过类名+()实现的
bart = Students('Bart Simpson', 59)
print(bart)
print(Students)


# 可以看到，变量bart指向的就是一个Student的实例，后面的数字是内存地址，每个object的地址都不一样，而Students本身就是一个类

# bart.name = 'Bart Simpson'
print(bart.name)


# 由于类可以起到模版的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把需要的属性绑上去
# __init__方法的第一个参数永远是self，表示创建的实例本身
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
print(bart.score)

# 和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
# 并且调用时，不用传递该参数


# 数据封装
# 面向对象编程的一个重要特点就是数据封装，在上面的Students类中，每个实例就拥有各自的name和score这些数据
# 我们可以通过函数来访问这些数据
def print_score(std):
    print('%s: %s' % (std.name, std.score))


print_score(bart)

# 但是，既然Students实例本身就拥有这些数据，要访问这些数据，就没有必要从外卖的函数去访问，
# 可以直接在Students类的内部定义访问数据的函数，这样，就把“数据”封装起来类
# 这些封装数据的函数是和Studengs类本身是关联起来的，我们称之为类的方法
bart.print_score()
print(bart.get_grade())