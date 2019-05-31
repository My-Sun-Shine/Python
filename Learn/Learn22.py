# type() 判断这个变量是个什么类型的对象
# 注意不要格式化该文件，导入模块顺序不能变
import sys
import os
# __file__是获取执行文件的相对路径，这个语句是获取上一级的上一级目录
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import types
#顺序一定这样写，先把项目路径加入到Path，才能导入 自定义模块不会报错
from Learn.Learn21 import Animal,run_2

print(type(123))
print(type(23.23))
print(type("str"))
print(type(None))
print(type(abs))
print(type(Animal()))
print(type(123) == type(456))
print(type(123) == int)
print(type(123) == type(123.123))
print(type(123) == type("123"))
print(type(run_2) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(1, 10))) == types.GeneratorType)

# isinstance 来判断某个变量是不是某个类型
# 这样一次性判断是否是某些类型的其中一个
print(isinstance([1,2,3],(list,tuple,dict)))
print(isinstance((1,2,3),(list,tuple,dict)))

# dir() 方法获取一个对象上的所有属性和方法
# print(dir("sss"))
# print(dir(dict))
print(dir(Animal))

# getattr()、setattr()，hasattr() 分别是获取某个属性值，设置某个属性值，判断是否有某个属性
class MyObject(object):
    def __init__(self):
        self.x = 8
    def print_my(self):
        print("AAAAAAAA")
obj = MyObject()    
print(hasattr(obj,"x"))
print(hasattr(obj,"y"))
print(getattr(obj,"x"))
# print(getattr(obj,"y")) #获取一个不存在的属性 会报错
print(getattr(obj,"y",404)) # 设置报错返回值
print(setattr(obj,"y","YYY"))
print(getattr(obj,"y"))
# 还可以对方法进行操作
print(hasattr(obj,"print_my"))
obj_method = getattr(obj,"print_my")
obj_method()