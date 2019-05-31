# 字符串和编码
# ord()获取字符的整数表示
print(ord("A"))  # 65
print(ord("中"))  # 20013
# chr()把编码转换为对应的字符串
print(chr(65))  # A
print(chr(25991))  # 文

print("\u4e2d\u6587")  # 16进制表示 中文

print(b"ABC")  # bytes类型的数据
print("ABC".encode("ASCII"))  # b'ABC'
print("中文".encode("UTF-8"))  # b'\xe4\xb8\xad\xe6\x96\x87'
# print("中文".encode("ASCII"))#报错
print(b"ABC".decode("ASCII"))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("UTF-8"))
# 加上errors="ignore"忽略错误
print(b"\xe4\xb8\xad\xff".decode("utf-8", errors="ignore"))

print(len("ABC"))  # 3
print(len("中文"))  # 2
print(len(b"ABC"))  # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 6

# 占位符
print("Hi,%s,you have %d." % ("Mark", 20000))  # Hi,Mark,you have 20000.
print("%2d-%02d" % (3, 1))  # 3-01
print("%.2f" % 3.1415926)  # 3.14
print("Age:%s. Gender:%s" % (25, True))  # Age:25,Gender:True
print("%d %%" % 7)  # 7% 使用%%来表示一个%

# format()函数
# hello, xiaoming,成绩提高了18.1%
print("hello, {0},成绩提高了{1:.1f}%".format("xiaoming", (85-72)/72*100))
