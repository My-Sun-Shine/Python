# 装饰器 不修改函数本身的定义，在代码运行期动态的增加功能的方法
import functools
import time
from datetime import date
from datetime import datetime


def now():
    print(date.today())


now()
f = now
f()
print(now.__name__, " ", f.__name__)  # 对于每个函数 都有一个属性__name__的属性
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


def log_1(func):
    # 定义一个decorator高阶函数
    def log_now(*arg, **kw):  # 这样写说明装饰的那个函数可以接收任何参数
        print("call %s()" % func.__name__)
        return func(*arg, **kw)
    return log_now


@log_1  # 这个就是装饰器
def now_1():
    print(date.today())


# 把@log_1放在函数定义处，相当于执行 now_1 = log_1(now_1)
now_1()  # 此时调用方法，会先打印一串日志，在执行方法
print(now_1.__name__)


def log_2(text):
    def func_decorator(func):
        def log_now(*arg, **kw):  # 这样写说明装饰的那个函数可以接收任何参数
            print("%s %s()" % (text, func.__name__))
            return func(*arg, **kw)
        return log_now
    return func_decorator


@log_2("参数")  # 这个就是装饰器
def now_2():
    print(date.today())


# now_2=log_2("参数")(now_2)
now_2()  # 首先调用了log_2("参数")，返回func_decorator函数，然后使用func_decorator函数，参数是now_2进行调用
print(now_2.__name__)  # 此时的name属性已经被装饰函数log_name的name属性

# 下面我们需要把__name__变回原来的————————————————————————————————————————————————————————————————————————————————————


def log_3(text):
    def func_decorator(func):
        @functools.wraps(func)  # 使用这句函数，就是把__name__变回原来的
        def log_now(*arg, **kw):  # 这样写说明装饰的那个函数可以接收任何参数
            print("%s %s()" % (text, func.__name__))
            return func(*arg, **kw)
        return log_now
    return func_decorator


@log_3("参数")  # 这个就是装饰器
def now_3():
    print(date.today())


now_3()
print(now_3.__name__)  # now_3


def metric(func):
    # 设计一个decorator函数，作用于任何函数上，并打印函数执行的时间
    @functools.wraps(func)
    def functime(*args, **kw):
        # ticks_s = datetime.now()
        ticks_s = time.time()  # 秒
        # ticks_s = time.clock() # 秒
        print(ticks_s)
        func(*args, **kw)
        # ticks_end = datetime.now()
        ticks_end = time.time()  # 秒
        # ticks_end = time.clock() # 秒
        print(ticks_end)
        print("%s exec %.2f ms" % (func.__name__, (ticks_end-ticks_s)*1000))
    return functime


@metric
def fast(x, y):
    time.sleep(5)
    print(x+y)


fast(1, 2)
