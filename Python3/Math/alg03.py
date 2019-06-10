# 杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1


def triangles(n):
    L = [1]
    line = 1
    while line <= n:
        print(L)
        L_new = [1]
        for i in range(0, len(L)):
            if i < len(L)-1:
                L_new.append(L[i]+L[i+1])
            else:
                L_new.append(L[i])
        L = L_new
        line = line+1


triangles(10)


def triangles_g(n):
    # generator函数
    L = [1]
    line = 1
    while line <= n:
        yield L
        L_new = [1]
        for i in range(0, len(L)):
            if i < len(L)-1:
                L_new.append(L[i]+L[i+1])
            else:
                L_new.append(L[i])
        L = L_new
        line = line+1


g = triangles_g(10)
for x in g:
    print(x)
