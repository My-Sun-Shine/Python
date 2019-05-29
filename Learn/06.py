import math  # 引入math模块
# 函数
# 空函数 什么都不做


def nop():
    pass  # 什么都不做，相当于一个占位符，这样程序可以运行


def my_abs(x):
    # isinstance(obejct,classinfo)判断object实参是classinfo实参的实例或者是子类的实例
    # 如果classinfo是对象类型的元组，那么如果object是其中任意一个的实例则返回true
    if not isinstance(x, (int, float)):
        raise TypeError("类型错误")  # 主动抛出异常
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx, ny  # 返回多个值


print(move(10, 10, 60, math.pi/2))


def quadratic(a, b, c):
    # ax2+bx+c=0
    if(a == 0):  # 非二元一次方程
        return (-c)/b
    num = b**2-4*a*c
    if(num < 0):  # 无解
        return
    x = math.sqrt(num)
    return (-b+x)/(2*a), (-b-x)/(2*a)


print(quadratic(2, 3, 1))  # -0.5,-1.0
print(quadratic(1, 3, -4))  # 1.0,-4.0
print(quadratic(1, 1, 1))
print(quadratic(0, 1, 1))
print(quadratic(-1, 1, 1))
