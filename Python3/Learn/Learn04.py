# 集合list 有序，可以修改删除添加的集合 查找和插入的时间随机元素的增多而增多不需要占用大量内存
classmates = ["AAA", "BBB", "CCC"]
print(classmates)
print(len(classmates))  # 3
print(classmates[0], classmates[1], classmates[2])
print(classmates[-1], classmates[-2], classmates[-3])
classmates.append("DDD")  # 添加一个元素
print(classmates)
classmates.insert(1, "EEE")  # 在指定位置插入一个元素
print(classmates)
classmates.pop()  # 删除结尾的元素
print(classmates)
classmates.pop(1)  # 删除指定位置的元素
print(classmates)
classmates[0] = "ABCD"  # 修改元素
print(classmates)
list1 = ["AAA", 123, True]
print(list1)  # 列表元素可以不一样
list2 = ["AAA", "BBB", ["AAA", "CCC"], "DDD"]
print(list2)  # 列表元素是列表
print(len([]))  # 空列表
list3 = [["AA", "BB", "CC"], ["DD", "EE", "FF", "GG"], ["HG", "IG", "JF"]]
print(list3[0][0], list3[1][1], list3[2][2], sep=" ")

# 元组tuple 有序但是一旦初始化就不能改变
classmates_T = ("AAA", "BBB", "CCC")
print(classmates_T)
tuple1 = (1,)  # 只有一个元素的tuple定义时必须加一个逗号
print(tuple1)
print(())  # 空tuple
tuple2 = ("A", "B", ["C", "D"])
print(tuple2)
tuple2[2][0] = "E"
tuple2[2][1] = "F"
print(tuple2)  # 这样是可以修改元组数据的，因为元组中第三个元素是列表，本身没有改变，但是列表元素可以发生改变

# 字典dict 键值对 查找和插入的时间不会因为元素的增多而变慢 需要占用大量内存
# key是不可变得对象，list对象是可变得不能作为key
dict1 = {'A': 95, 'D': 65, 'C': 78}
print(dict1['A'])
dict1['A'] = 100
print(dict1['A'])
# dict1['D'] # key不存在 会报错
print("C" in dict1)  # 判断是否存在dict
print(dict1.get("E"))  # get()方法，如果key不存在，返回none或者自己定义的value
print(dict1.get("C"))  # 如果存在,则返回对应value
print(dict1.get("E", -1))
print(dict1.get("E", 10))
dict1.pop("A")  # 删除某个键值对
print(dict1)

# set 一组key的集合，不存储value，key是不会重复的
set1 = set([1, 2, 34, 1, 2, 35, 56, 56])
print(set1)
set1.add(566)
set1.add(56)  # 添加重复数据没有任何效果
print(set1)
set1.remove(56)  # 移除某个key
print(set1)
set2 = set([1, 2, 3])
set3 = set([2, 3, 4])
print(set2 | set3)  # 并集
print(set2 & set3)  # 交集

# 对于可变对象，修改该对象，该对象本身会被修改，而对于不可变对象，修改本身，只会在内存中重新声明一个修改之后的结果，
list4 = ['b', 'c', 'a']
list4.sort()
print(list4)  # 可变对象
str1 = "ABC"
str1.replace("A", "a")
print(str1)  # 不可变对象

# 如何把列表["a","a","b","a","b","c"] 转换为字典{"a":3,"b":2,"c":1}
str_list = ["a", "a", "b", "a", "b", "c"]
str_dict = {}
for x in str_list:
    if(str_dict.get(x, -1) == -1):
        str_dict[x] = 1
    else:
        str_dict[x] = str_dict[x]+1
print(str_dict)

str_dict = {}
str_set = set(str_list)  # 把list转换为set 去重
str_dict = dict.fromkeys(str_set, 0)  # 把去重之后的set作为key，value都是0
for x in str_set:
    str_dict[x] = str_list.count(x)  # count(n)判断list中n这个元素的数量
print(str_dict)
