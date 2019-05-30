# 列表生成式 创建list
import os  # 引入os模块
print(list(range(1, 11)))
print([x*x for x in range(1, 11)])
print([x*x for x in range(1, 11) if x % 2 == 0])
print([m+n for m in "ABC" for n in "XYZ"])
print([d for d in os.listdir('..')])  # os.listdir可以列出文件和目录

dict1 = {"A": 1, "B": "b", "C": 56.6}
print([k+"="+str(v) for k, v in dict1.items()])
list1 = ["Hello", "World", "IBM", "Apple"]
print([s.lower() for s in list1])


list2 = ["Hello", "World", "IBM", "Apple", 18]
print([s.lower() for s in list2 if isinstance(s, str)])

# 关于if和for前后顺序的问题
print([num**2 for num in range(10) if num%2==0])#这是对for进行过滤
print([num**2 if num%2==0 else 0 for num in range(10) ])#这是对num**2的数进行if else判断
