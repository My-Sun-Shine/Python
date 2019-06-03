# 使用定制方法定制类
class Student(object):
    # __str__ 和 __repr__
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 用于print实例对象
        return "Student object (name:%s)" % self.name
    __repr__ = __str__  # 用于直接调用

    def __getattr__(self, attr):
        # 正常情况下 调用类中不存在的方法或属性，就会报错
        # 使用该方法可以动态返回一个属性或者方法
        if attr == "score":
            return 99
        if attr == "age":
            return lambda: 25

    def __call__(self):
        # 直接对实例调用，可以通过callable()判断实例是否为可以调用的对象
        # 只要实现该方法，callable函数就返回true
        print("My name is %s" % self.name)


s = Student("AA")
s()  # __call__
#只要实现 __call__方法，callable函数就返回true
print(callable(s), callable("str"), callable(True), callable([1, 2, 3, 4]), callable(None))

print(s)  # 不改写__str__的打印为 <__main__.Student object at 0x00000002F41A4240>

print("score:", s.score)  # __getattr__
print("age", s.age())


class Fib(object):
    # __iter__ 实现该类可以进行for in循环，该方法返回一个迭代对象
    # for循环就会不断调用该迭代对象的__next__方法，拿到循环的下一个值，直到遇见StopIteration()退出
    def __init__(self, n):
        self.a, self.b=0, 1
        self.n=n

    def __iter__(self):
        return self  # 返回迭代对象，实例本身

    def __next__(self):
        self.a, self.b=self.b, self.a+self.b
        if self.a > self.n:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # 虽然使用__iter__实现for，但终究不能像list一样使用
    def __getitem__(self, n):
        # 使用__getitem__获取元素，目前这个例子是当做list，但是还可以把对象看作dict
        # 与之对应的是__setitem__方法，把对象视作list和dict对集合进行赋值
        # 使用__delitem__ 方法，用来删除某个元素
        if isinstance(n, int):
            for x in range(n):  # n是索引
                self.a, self.b=self.b, self.a+self.b
            if self.a > self.n:
                raise ValueError("错了，超出界限")
            return self.a
        if isinstance(n, slice):  # n是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            L=[]
            for x in range(stop):
                self.a, self.b=self.b, self.a+self.b
                if x >= start:
                    L.append(self.a)
            if self.a > self.n:
                raise ValueError("错了，超出界限")
            return L


for n in Fib(20):
    print(n)
print("getitem[6]:", Fib(20)[6])
print("getitem[7]:", Fib(20)[7])
# print("getitem[8]:", Fib(20)[8])
print("[0:5]", Fib(20)[0:5])
print("[:7]", Fib(20)[:7])
# print("[:10]", Fib(20)[:10])
