# __slots__的使用
import timeit
from types import MethodType


class Learn23_1(object):
    pass


def setAge(self, age):
    self.age = age


# 对一个实例绑定方法和属性，对另一个实例是不起作用的
l = Learn23_1()
l.name = "AAAA"  # 对实例绑定属性
print(l.name)
l.setAge = MethodType(setAge, l)  # 给实例绑定方法
l.setAge(25)  # 调用实例方法
print(l.age)
# 也可以直接对class类绑定方法和属性，那就是对所有的实例都有用
l1 = Learn23_1()
Learn23_1.name = "CCC"
Learn23_1.setAge = setAge
print(l1.name)
l1.setAge(50)
print(l1.age)

# 1.使用__slots__限制实例可以添加的属性
# 并拒绝类创建__dict__和__weakref__属性以节约内存空间


class Learn23_2(object):
    # 使用__slots__限制实例可以添加的属性
    __slots__ = ("name", "age")  # 使用tuple定义允许绑定的属性名称


class Learn23_2_child(Learn23_2):
    # 子类不会继承父类的限制，__slots__只会对当前类的实例起作用，不会对继承的子类起作用
    # 除非子类也定义__slots__,子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
    pass


learn = Learn23_2()
learn.name = "DDD"
learn.age = 66
# learn.score = 99  # 报错AttributeError:，不能绑定
print(learn.name, learn.age)
Learn23_2.age = 56  # __slots__限制的只是当前类的实例，不能对类本身的属性添加起限制
print(learn.name, learn.age, learn.age)
learn_child = Learn23_2_child()
learn_child.name = "DDD"
learn_child.age = 66
learn_child.score = 99
print(learn_child.name, learn_child.age, learn_child.score)

# 在创建大量实例的情况下，使用__slots__可以减少近30%的内存消耗


class Foo(object):
    # 使用__slots__
    __slots__ = 'foo',


class Bar(object):
    pass


slotted = Foo()
not_slotted = Bar()


def get_set_delete_fn(obj):
    def get_set_delete():
        obj.foo = 'foo'
        obj.foo
        del obj.foo  # 删除实例
    return get_set_delete


a = min(timeit.repeat(get_set_delete_fn(slotted)))  # 计算时间最小
b = min(timeit.repeat(get_set_delete_fn(not_slotted)))
print(a)
print(b)
print(b/a)
