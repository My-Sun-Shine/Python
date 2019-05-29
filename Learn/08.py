# 递归函数
def fact(n):
    if n <= 1:
        return 1
    else:
        return n+fact(n-1)


print(fact(15))  # 5


def fact_1(n):
    return fact_iter(n, 1)


def fact_iter(n, x):
    if n == 1:
        return x
    else:
        return fact_iter(n-1, n+x)

print(fact_1(15))