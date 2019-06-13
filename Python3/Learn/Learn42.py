# 集合模块
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter

##############################################################################################################################
# namedtuple可以创建一个自定义的tuple对象，并且规定tuple元素的个数，并使用属性而不是索引来引用
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))
Circle = namedtuple("Circle", ["x", "y", "z"])

##############################################################################################################################
# deque高效实现插入和删除操作的双向列表，适用于队列和栈
# 实现list的append()和pop()，获取appendleft()和popleft()方法对头部进行添加或删除元素
q = deque(["a", "b", "c"])
q.append("x")
q.appendleft("y")  # 左边加
print(q)

##############################################################################################################################
# defaultdict 使用dict时，如果引用的key不存在，就会抛出keyError
# 使用defaultdict，如果key不存在，则返回默认值，功能与dict一样
dd = defaultdict(lambda: "N/A")
dd["key1"] = 555
print(dd["key1"])
print(dd["key2"])

##############################################################################################################################
# OrderedDict保证key在添加时的顺序，dict本身是无序的
d = dict([("a", 1), ("b", 2), ("c", 3)])
print(d)
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print(od)


class LastUpdateOrderDict(OrderedDict):
    # 实现一个先进先出的dict，当容量超出限制，先删除最早添加的key
    def __init__(self, count):
        super(LastUpdateOrderDict, self).__init__()
        self._count = count

    def __setitem__(self, key, value):
        containkey = 1 if key in self else 0  # 判断是否有重名的key
        if len(self)-containkey >= self._count:
            # self.popitem方法默认删除并返回字典最后一个元素，、
            # self.popitem(last=False)则是删除并返回第一个被添加的元素
            last = self.popitem(last=False)
            print("remove", last)
        if containkey:
            del self[key]
            # 是否有重复的,有重复并不是简单的替换，而是把原先的删除，并添加
            print("set:", (key, value))
        else:
            print("add:", (key, value))
        OrderedDict.__setitem__(self, key, value)


luod = LastUpdateOrderDict(3)
luod["z"] = 1
luod["x"] = 2
luod["a"] = 3
luod["b"] = 5
luod["b"] = 3
luod["a"] = 3
print(luod)

##############################################################################################################################
# ChainMap 将多个字典或者其他映射组合在一起，创建一个单独可更新的视图
dict1 = {"a": "a1", "b": "b1"}
dict2 = {"c": "c1", "d": "d1"}
dict3 = {"c": "c2", "f": "f1"}
cm = ChainMap(dict1, dict2, dict3)
print(cm)
print(list(cm))
print(cm["c"])

##############################################################################################################################
# counter 计数器
c = Counter()
c.update("programming")
print(c)

c = Counter("programming")
print(c)
