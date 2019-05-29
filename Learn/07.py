# 函数的参数
# 默认参数################################################################################################################################################################


def power(x, n=2):
    return x**n


def add_end(L=[]):
    L.append("End")
    return L


def add_end_None(L=None):
    if L is None:
        L = []
    L.append("End")
    return L


print(power(5, 3))
print(add_end(["a", "b"]))  # ['a', 'b', 'End']
print(add_end([1, 2, 3]))  # [1, 2, 3, 'End']

L1 = [1, 2, 3]
print(add_end(L1))  # [1, 2, 3, 'End']
print(L1)  # [1, 2, 3, 'End'] L1已经发生改变

# 默认参数L是一个变量，指向对象[],每次调研该函数，如果改变L的内容，则下次调用的时候，默认参数的内容就变了，不再是函数定义时的[]
print(add_end())  # ['End']
print(add_end())  # ['End', 'End']
print(add_end())  # ['End', 'End', 'End']
# 定义默认参数，默认参数必须指向不变对象
print(add_end_None())  # ['End']
print(add_end_None())  # ['End']
print(add_end_None())  # ['End']

# 可变参数################################################################################################################################################################


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n
    return sum


print(calc(1, 2, 3))  # 6
print(calc(1, 2, 3, 5))  # 11
# 如果已经有一个list或者tuple 需要调用一个可变参数
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))  # 6
print(calc(*nums))  # 6 python允许在list或者tuple类型变量前面加一个*号，把参数变成可变参数传入

# 关键字参数################################################################################################################################################################
# 关键字参数允许传入0个或任意个含参数名参数，这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


person("AAA", 45)  # name: AAA age: 45 other: {}
# name: AAA age: 45 other: {'city': 'Beijing'}
person("AAA", 45, city="Beijing")
# name: AAA age: 45 other: {'city': 'Beijing', 'job': '工程师'}
person("AAA", 45, city="Beijing", job="工程师")
extra = {"city": "Beijing", "job": "工程师"}
# name: AAA age: 45 other: {'city': 'Beijing', 'job': '工程师'}
person("CCC", 65, city=extra["city"], job=extra["job"])
# **extra是吧extra这个dict的所有key-value用关键字参数传入到函数中，kw将会得到extra的一份拷贝，对kw进行改动不会影响函数外的extra
# name: AAA age: 45 other: {'city': 'Beijing', 'job': '工程师'}
person("SSS", 45, **extra)
print(extra)  # {'city': 'Beijing', 'job': '工程师'}

# 命名关键字参数################################################################################################################################################################


def person_1(name, age, **kw):
    if "city" in kw:
        kw.pop("city")
    if "job" in kw:
        kw.pop("job")
    print("name:", name, "age:", age, "other:", kw)


# name: SSSA age: 55 other: {'addr': 'aaa'}
person_1("SSSA", 55, addr="aaa", city="ccc")


def person_2(name, age, *, city, job):
    # 这样用来限制关键字参数的名称，这就是命名关键字，只接收city和job作为关键字参数
    # 命名关键字参数必须传入参数没那个，不能缺少
    # 可以对命名关键字参数设置默认值，这样可以不传
    print("name:", name, "age:", age, "city:", city, "job:", job)


# name: SSSA age: 55 city: ccc job: aaa
person_2("SSSA", 55, job="aaa", city="ccc")

#多个参数组合###########################################################################################################################################


def f1(a, b, c=0, *args, **kw):
    print("a:", a, "b:", b, "c:", c, "args:", args, "kw", kw)


def f2(a, b, c=0, *, d, **kw):
    print("a:", a, "b:", b, "c:", c, "d:", d, "kw", kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, "a", "c")
f1(1, 2, 3, "a", "c", X=99)
f2(1, 2, 3, d=99, ext="aa")

args = (1, 2, 3, 4)
kw = {"d": 99, "X": "AS"}
f1(*args, **kw)
args = (1, 2, 3)
f2(*args, **kw)


# 可以接收一个或者多个数并计算乘积
def product(*array):
    num = 1
    for x in array:
        num = num*x
    print(num)

product(5)  # 5
product(5, 6)  # 30
product(5, 6, 7)  # 210
product(5, 6, 7, 9)  # 1890
