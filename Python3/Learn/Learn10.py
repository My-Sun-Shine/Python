# 迭代
# Python的for循环不仅可以用在list或tuple上，还可以作用于其他可迭代对象
from collections import Iterable  # 判断是否可以迭代

dict1 = {"A": 1, "B": "b", "C": 56.6}
for key in dict1:
    print("key:", key)
for value in dict1.values():
    print("value:", value)
for key, value in dict1.items():
    print(key, ":", value)

for ch in "ABCD":
    print(ch)

# 判断是否可以迭代
print(isinstance("AAAA", Iterable))
print(isinstance([1, 2, 3, 4], Iterable))
print(isinstance(123, Iterable))

# Python内置的enumerate函数可以把list转换为索引-元素对
for i, value in enumerate(["a", "b", "c"]):
    print(i, value)

for x, y in [(1, 2), (2, 4), (3, 6)]:
    print(x, y)

# 使用迭代查找一个list中最小的最大值，并返回一个tuple


def finMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    if len(L) == 1:
        return (L[0], L[0])
    minNum = L[0]
    maxNum = L[0]
    for x in L:
        if x > maxNum:
            maxNum = x
        if x < minNum:
            minNum = x
    return (minNum, maxNum)


print(finMinAndMax([]))
print(finMinAndMax([7]))
print(finMinAndMax([7, 1]))
print(finMinAndMax([7, 1, 3, 9, 5]))
