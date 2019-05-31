# 生成器generator
# 如果创建一个包含大量数据的列表,会占用大量内存，所以可以采取不创建完整的list，使用一种叫做生成器的generator机制
# 该机制可以一边循环一边计算
# 下面两种 使用[]的是list 而使用()则是generator
print([x*x for x in range(10)])
print((x*x for x in range(10)))

g1 = (x*x for x in range(5))
# 使用next()函数获取generator下一个返回值
print(next(g1))  # 0
print(next(g1))  # 1
print(next(g1))  # 4
print(next(g1))  # 9
print(next(g1))  # 16
# print(next(g1))#超出界限报错
for g in g1:  # 可以使用for循环，generator是可迭代对象
    print(g)




def odd():
    # 返回值是generator的函数
    # 函数是顺序执行的，遇到return语句或者最后一行函数语句就返回，
    # 但是generator函数，在每次调用next()的时候，遇到yield语句就会返回，下一次执行的时候从上次返回的yield语句处开始
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3


o = odd()
next(o)
next(o)
next(o)

