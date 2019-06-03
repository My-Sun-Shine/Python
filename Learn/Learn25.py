# 多重继承类 一个子类继承父类所有的功能
class Animal(object):
    # 动物基类
    pass


class Mammal(object):
    # 哺乳动物
    pass


class Bird(object):
    # 鸟类
    pass


class Runnable(object):
    # 会跑的动物
    def run(self):
        print("我是会跑的动物")


class Flyable(object):
    # 会飞的动物
    def fly(self):
        print("我是会飞的动物")


class Dog(Mammal, Runnable):
    # 狗 哺乳动物 会跑
    pass


class Bat(Mammal, Flyable):
    # 蝙蝠 哺乳动物 会飞
    pass


class Ostrich(Bird, Runnable):
    # 鸵鸟
    pass
