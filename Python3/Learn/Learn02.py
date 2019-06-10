# 输出函数
print("测试", "函数", "print")
print(300)
print(100+200)
print("100 + 200 =", 100+200)

# 输入函数
# name = input()
# print("Hello,", name)

# 数据类型包括 整数、浮点数、字符串、布尔型、空值
print(0xff00)  # 整数
print(1.23e9)  # 浮点数
# 字符串
print("I\'m \"OK\"!")
print("I\'m learning\nPython")
print("\\\t\\")
print(r"\\\t\\")  # r''表示''内部的字符串默认不转义
print('''line1
...line2
...line3''')  # 允许用'''...'''的格式表示多行内容
# 布尔型
print("3>5: ", 3 > 5)
print("True and False: ", True and False)
print("True or False: ", True or False)
print("not 1>2: ", not 1 > 2)
print(None)  # 空值

# 变量 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
t_007 = "T800"
print(t_007)
a = 'ABC'  # 在内存里面创建一个'ABC'的字符串，并创建一个名为a的变量，并将该变量指向'ABC'
b = a  # 将变量b指向变量a所指向的数据，即'ABC'
a = 'XYZ'  # 在内存里面创建一个'XYZ'的字符串，并将变量a指向'XYZ'，但是b没有改变
print(b)  # 输出 ABC

# 常量：不能改变的变量，在Python中通常使用全部大写的变量名表示常量
PI = 3.14159265359

# /、//、%的区别
print(10/3)  # 3.3333333333333335
print(9/3)  # 3.0
print(10//3)  # 3
print(10 % 3)  # 1
