# 高阶函数：map()、reduce()、filter()、sorted()###################################################################################################
# 函数作为参数
# 下面使用到了匿名函数 语法：lambda 参数列表:返回值，例如lambda x:x*x；不用写return
from functools import reduce
print(abs)  # 输出 函数变量
fabs = abs  # 把函数赋值到变量上
print(fabs(-5))  # 使用该变量


def add(x, y, f):
    # 定义一个函数，参数是一个函数，这种就是高阶函数
    return f(x)+f(y)


print(add(-5, 6, abs))

# map()函数#################################################################################################################
# map()函数接收两个参数，第一个是函数，第二个是Iterable对象
# map会将序列的每个元素传入函数，并把结果作为Iterator返回


def mapf(x):
    return x*x


print(map(mapf, range(1, 10)))
print(list(map(mapf, range(1, 10))))
print(list(map(str, range(1, 10))))  # 把list中的数字转换为字符串


def normalize(name):
    # 把每个英文字符串，变成首字母大写，其他小写的规范名字
    if isinstance(name, str):
        return name[0].upper()+name[1:].lower()


names = ["adam", "LIAS", "barT"]
print(list(map(normalize, names)))

# reduce()函数#################################################################################################################
# reduce把一个函数作用于一个序列[x1,x2,x3,...],这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累计计算
# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)


def fn(x, y):
    return x*10+y


def char2num(s):
    return int(s)


print(list(map(char2num, "123456")))
print(reduce(fn, map(char2num, "123456")))
# 使用lambda进行简化
print(reduce(lambda x, y: x*10+y, map(lambda x: int(x), "123456")))

print(reduce(lambda x, y: x*y, [3, 7, 5, 9]))

s1, s2 = "123.456".split(".")
print(s1+s2)
print(reduce(fn, map(char2num, s1+s2))/(10**len(s2)))

# filter()函数#################################################################################################################
# filter函数同样第一个参数为函数，第二个参数是序列，该函数返回的是Iterator
# 只是filter把传入的函数依次作用于每个元素，然后安装函数的返回值是true还是false判断是否保留该元素
print(list(filter(lambda x: x & 2 == 0, range(1, 10))))  # 保留偶数


def to_palindrom(n):
    # 判断是否是回数
    if isinstance(n, int):
        strn = str(n)
        count = len(strn)
        for i in range(0, count//2):
            if strn[i] != strn[count-1-i]:
                return False
        return True
    else:
        return False


print(list(filter(to_palindrom, range(1, 200))))

# sorted()函数#################################################################################################################
# sorted函数第一个参数是序列，第二个参数(可选关键字参数)是一个key接收函数，它通过接收一个key函数实现自定义排序
# 第三个布尔参数reverse 实现是否反向排序

List1 = [36, 5, -12, -5, 23, 0]
print(sorted(List1))  # 按实际大小排序
print(sorted(List1, key=abs))  # 按绝对值排序

List2 = ["bob", "about", "Zoo", "Credit"]
print(sorted(List2))  # 这是按ASCII的大小比较排序，Z<a 所以Z在a前面
print(sorted(List2, key=str.lower))  # 按照小写排序
print(sorted(List2, key=str.lower, reverse=True))  # 排序翻转

List3 = [("Bob", 75), ("Adam", 95), ("Bart", 66), ("Liss", 88)]
print(sorted(List3, key=lambda n: n[0]))  # 按名字排序
print(sorted(List3, key=lambda n: n[1], reverse=True))  # 按成绩从大到小排序
