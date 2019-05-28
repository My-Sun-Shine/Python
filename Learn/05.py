# if else语句
height = 1.75
weight = 80.5
bmi = weight/(height**2)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
elif bmi >= 32:
    print("严重肥胖")
else:
    print("错误")

# for in
names = ["AA", "CC", "DD"]
for name in names:
    print(name)

sumNum = 0
for x in range(101):  # range(n) 生成0到n-1的整数序列
    sumNum = sumNum+x
print(sumNum)

# while
sumNum = 0
n = 0
while n <= 100:
    sumNum = sumNum+n
    n = n+1
print(sumNum)

#break continue
