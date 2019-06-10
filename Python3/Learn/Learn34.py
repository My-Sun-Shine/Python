# 从内存中读取 StringIO和BytesIO
from io import StringIO
from io import BytesIO
f = StringIO("Hello,World\nHello,World")
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())
print(f.tell())  # 获取读取指针的位置
f.seek(0)  # 用seek把指针复原
# seek方法 第一个参数向前或前后的偏移量，正为后，负为前；第二个参数，可选，默认为0表示文件开头，1表示当前位置，2表示文件末尾
print(f.read())  # 指针会发生移动

f1 = StringIO()
f1.write("Hello,World!\n")
f1.write("Hello,World!")
print(f1.getvalue())  # 不会影响指针

b = BytesIO()
b.write("中文".encode("utf-8"))
print(b.getvalue())
print(list(b.getbuffer()))

b1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b1.read())
