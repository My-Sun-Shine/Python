# itertools 提供用于操作迭代对象的函数
import itertools
# count创建一个无限迭代自然数序列
natuals = itertools.count(1, 2)  # 从1开始，2为步长
# for n in natuals:
#    print(n)

cs = itertools.cycle("ABC")  # cycle 会按A、B、C、A、B、C、A....这样的顺序无限下去

# repeat会把一个元素重复下去，第二个参数是重复次数，不指定则是无限重复
ns = itertools.repeat("A", 3)
for n in ns:
    print(n)

# takewhile会根据条件判断，截取一个序列出来
tw = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(tw))

# chain可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain("ABC", "ASSS"):
    # 依次输出 A B C A S S S
    print(c)

# groupby把相邻的重复元素放在一起，这是区分大小写的
for key, group in itertools.groupby("AAASDSDDDDDBb"):
    print(key, list(group))
# A ['A', 'A', 'A']
# S ['S']
# D ['D']
# S ['S']
# D ['D', 'D', 'D', 'D', 'D']
# B ['B']
# b ['b']

# 不区分大小写
for key, group in itertools.groupby("AaaSDSdddDDBb", lambda c: c.upper()):
    print(key, list(group))

# A ['A', 'a', 'a']
# S ['S']
# D ['D']
# S ['S']
# D ['d', 'd', 'd', 'D', 'D']
# B ['B', 'b']

#############################################################################################################


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda n: n < 2*N, natuals)
    sum = 0
    zhengfu = True
    for n in ns:
        if zhengfu:
            sum += (4/n)
        else:
            sum -= (4/n)
        zhengfu = not zhengfu
    return sum


def pi_1(N):
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda n: n < 2*N, natuals)
    pm = list(ns)
    result = list(map(lambda x: float(4/x if pm.index(x) %
                                      2 == 0 else 4/x*-1), pm))

    return sum(result)


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
print(pi_1(10))
print(pi_1(100))
print(pi_1(1000))
print(pi_1(10000))
