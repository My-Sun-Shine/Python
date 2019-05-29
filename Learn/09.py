# 切片操作

list1 = ["AA", "BB", "CC"]
# 从索引0开始取，直到索引3为止，但不包括索引3
print(list1[0:3])  # ['AA', 'BB', 'CC']
print(list1[:3])  # ['AA', 'BB', 'CC']
print(list1[1:3])  # ['BB', 'CC']
print(list1[-2:])  # ['BB', 'CC']
print(list1[-2:-1])  # ['BB']
print(list1[-2:0])  # []
print(list1[:])  # 什么都不写 原样

list2 = list(range(100))  # [0,1,2,3,4....,99]
print(list2[:10])  # 取前10个
print(list2[-10:])  # 取后10个
print(list2[:10:2])  # 前10个中，每两个取一个[0, 2, 4, 6, 8]
print(list2[::10])  # 每十个取一个[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

tuple1 = (1, 2, 3, 4, 5)
print(tuple1[:2])

print("ABCDEFG"[:3])

# 利用切片操作，实现trim函数，去掉字符串首尾的空格，不能使用str的strip()


def trim(str_1):
    if not type(str_1) is str:
        raise TypeError
    start = 0
    end = 0
    count = len(str_1)
    for n in range(count):
        if str_1[n] != " ":
            start = n
            break
    for n in range(count):
        if str_1[count-1-n] != " ":
            end = count-1-n
            break
    return str_1[start:end+1]


print(trim("hello   "))
print(trim("   hello"))
print(trim("  hello  "))
print(trim("   hello world   "))
print(trim(""))
print(trim("     "))
