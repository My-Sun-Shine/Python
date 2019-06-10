# 偏函数
import functools


def int2(x):
    return int(x, base=2)  # base=2 就是传入的是二进制字符串，转换为十进制数字


# 把一个函数的某些参数给固定住，也就是设置默认值，返回一个新的函数
# functools.partial偏函数有三个参数，函数本身，*args，**kw
int2_p = functools.partial(int, base=2)

print(int2("1000"))
print(int2_p("1000"))  # 相当于 kw={"base":2} int("1000",**kw)
