# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax+x
        return ax
    return sum


f = lazy_sum(1, 2, 3, 5)
f_1 = lazy_sum(1, 2, 3, 5)
print(f)
print(f())
print(f == f_1)  # 这两个互相不影响


def count_9():
    fs = []
    for i in range(1, 4):
        fs.append(lambda: i*i)
    return fs


f1, f2, f3 = count_9()
print(f1(), f2(), f3())  # 结果全是9 是因为等到三个函数返回之后，i已经变成的了3
## 注意： 返回闭包时，返回函数不要引用任何循环变量，或者后续会发生变化的变量###############################


def count():
    def f(i):
        return lambda: i*i
    fs = []
    for n in range(1, 4):
        fs.append(f(n))
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 利用闭包返回一个计数器函数，每次调用它返回一个递增函数
counterA = createCounter_3()
print(counterA(), counterA(), counterA(), counterA(), counterA())


def createCounter_1():
    i = 0  # 这是不可变类型变量

    def counter():
        while True:
            nonlocal i  # 使用外层变量
            i = i+1
            return i
    return counter


def createCounter_2():
    i = [0]  # 这是可变类型变量

    def counter():
        i[0] = i[0]+1
        return i[0]
    return counter


def createCounter_3():
    def f():
        n = 1
        while True:
            yield n
            n += 1
    fn = f()  # generator函数

    def counter():
        return next(fn)
    return counter
