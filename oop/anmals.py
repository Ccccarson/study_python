# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）


class Animal(object):
    def run(self):
        print('Animal is running...')

# 当我们需要便携dog和cat类时，就可以直接从animal类继承


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print("Eating meat...")


class Cat(Animal):
    def run(self):
        print('Cat is Running...')

# 继承最大的好处时子类获得父类的全部功能
# 当子类和父类都存在相同的方法时，我们就说，子类的方法覆盖了父类的方法，
# 代码运行时，总会调用子类的方法，这样，我们就获得了继承的另一个好处：多态

# 多态的好处就是，当我们需要传入子类时，只需要接受父类类型就可以了


dog = Dog()
dog.run()

cat = Cat()
cat.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Cat())
run_twice(Animal())