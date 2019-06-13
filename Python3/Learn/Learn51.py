# 上下文管理器 __enter__和__exit__
# 简单实现上下文管理器
from contextlib import contextmanager, closing
from urllib.request import urlopen


class Query1(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("进入上下文管理")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Error")
        else:
            print("退出上下文管理")

    def query(self):
        print("name:", self.name)


with Query1("aaaa") as target:
    # 任何对象都能实现上下文管理，用于with语句
    target.query()
print("————"*10)

###############################################################################################################
# Python的标准库contextlib提供了更简单的写法


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print("name:", self.name)


@contextmanager
def create_query(name):
    print("begin")
    q = Query(name)
    yield q
    print("end")


with create_query("aaaa") as target:
    target.query()
print("————"*10)

############################################################
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


# with语句首先执行yield之前的语句
# yield语句会调用with内部的所有语句
# 最后执行yield之后的语句
with tag("h1"):
    print("hello,world")


# closing也是一个经过@contextmanager装饰的generator
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()
with closing(urlopen('https://www.python.org')) as target:
    for line in target:
        print(line)
    

