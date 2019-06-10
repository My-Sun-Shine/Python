# 迭代器
# 可以进行for循环的数据类型
# 1.集合数据类型，如list、tuple、dict、set、str等，这些属于Iterable对象
# 2.generstor，包括生成器和带yield的generator函数，这些属于Iterator对象
from collections import Iterable  # 判断是否可以迭代
from collections import Iterator  # 判断是否是迭代器

# 判断是否可以迭代
print(isinstance("AAAA", Iterable))  # true
print(isinstance([1, 2, 3, 4], Iterable))  # true
print(isinstance(123, Iterable))  # false

# 判断是否是迭代器
print(isinstance("AAAA", Iterator))  # false
print(isinstance([1, 2, 3, 4], Iterator))  # false
print(isinstance(123, Iterator))  # false
print(isinstance((x for x in range(10)), Iterator))  # true

# 使用iter()函数 把list、dict、str等Iterable对象转换为Iterator对象
print(isinstance(iter("AAAA"), Iterator))  # true
print(isinstance(iter([1, 2, 3, 4]), Iterator))  # true
