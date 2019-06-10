# 给函数默认参数赋值可变对象的Bug问题
# 默认参数不要默认为可变对象，要使用不可变对象


def extendList(val, L=[]):
    L.append(val)
    return L


# 两种输出方式分开运行
# 第一种输出方式
# print(extendList(10))  # [10]
# print(extendList(123, []))  # [123]
# print(extendList('a'))  # [10,'a']

# 第二种输出方式
list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
print(list1)  # [10,'a']
print(list2)  # [123]
print(list3)  # [10,'a']

# 运行结果分析
# 第一个extendList(10)在调用时，没有指定默认参数L，调用接受后，默认参数L变成了[10]，list1和L引用相同的内存地址
# 第二个extendList(123, [])是已经传入了默认参数[]，所以与第一个函数所引用的默认参数不是同一个，返回结果为[123]
# 第三个extendList('a')与第一个extendList(10)引用相同的默认参数L，但运行第一个时，L变成了[10]，
# 所以第三个函数运行时，默认参数L已经是[10]，第三个把L修改为[10,'a']，list3得到[10,'a']，
# 但是因为第三个与第一个引用相同的L，所以第一个的结果list1也变成了[10,'a']
# 第一种输出方式，也应该与第二种是相同结果，只是print(extendList(10)直接把一开始结果输出了
# 如果两种输出方法一块运行则是：
# [10]
# [123]
# [10, 'a']
# [10, 'a', 10, 'a']
# [123]
# [10, 'a', 10, 'a']


def extendList_new(val, L=None):
    # 建议写法
    if L is None:
        L = []
    L.append(val)
    return L


print(extendList_new(10))  # [10]
print(extendList_new(123, []))  # [123]
print(extendList_new('a'))  # ['a']
list1 = extendList_new(10)
list2 = extendList_new(123, [])
list3 = extendList_new('a')
print(list1)  # [10]
print(list2)  # [123]
print(list3)  # ['a']
