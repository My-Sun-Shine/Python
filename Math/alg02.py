# 斐波拉契数列，除了第一个数和第二个数，任意一个数都可以有前两个数相加得到
# 1,1,2,3,5,8,13,21,34,....


def fid(n):
    # n是前几个数
    i = 0
    a1 = 1
    a2 = 1
    while i < n:
        print(a1)
        a1, a2 = a2, a1+a2
        i = i+1

fid(11)

def fid_g(n):
    #generator函数 Learn/12.py
    i = 0
    a1 = 1
    a2 = 1
    while i < n:
        yield a1
        a1, a2 = a2, a1+a2
        i = i+1

for g in fid_g(11):
    print(g)