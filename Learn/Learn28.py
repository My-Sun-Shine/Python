# type()方法创建一个class对象，依次传入三个参数：
# 1.class的名
# 2.继承的父类集合，如果只有一个父类，注意tuple一个元素的用法写法
# 3.class的方法名称与绑定，比如把函数fn绑定到hello中


def fn(self, name="world"):
    print("Hello,", name)


Hello = type("Hello", (object,), dict(hello=fn))
Hello().hello()

# 元组 metaclass
# __new__()方法的参数依次是：当前准备创建类的对象，类的名称，类继承的父类集合，类的方法集合


class ListMetaclass(type):
    # metaclass是类的模板，所以必须从type类继承
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    # 解释器在创建MyList时，要通过ListMetaclass.__new__来创建
    pass


L = MyList()
L.add(1)
print(L)
