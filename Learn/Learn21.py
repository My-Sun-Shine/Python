# 类的三大特性 继承和多态
class Animal(object):
    # 这个是基类，它继承了object
    def run(self):
        print("跑起来......")


class Dog(Animal):
    # 这个是Animal的子类，它继承了Animal
    def run(self):
        print("狗应该咋跑.....")


class Cat(Animal):
    # 这个是Animal的子类，它继承了Animal
    pass


class GoGO(object):
    def run(self):
        print("come on gogo.....")


animal = Animal()
dog = Dog()
dog.run()  # 当子类和父类都存在相同的run()方法是，子类的run()会把父类的run()方法覆盖掉
cat = Cat()
cat.run()  # 子类会继承父类的一切

print(isinstance(dog, Dog))  # true
print(isinstance(cat, Cat))  # true
print(isinstance(cat, Animal))  # true 这一点和C#一样，if 子类 is 父类，这是对的
print(isinstance(animal, Cat))  # 这个就不对的 父类 not is 子类


def run_2(n):
    # 这就是多态了，，和java C#很像
    # 但是n参数不需要接收Animal类型或者其子类类型的实参，只有传过来的类实例有run()方法就行
    # 这就python动态语言的特性
    n.run()
    n.run()


run_2(dog)
run_2(GoGO())  # python动态语言
