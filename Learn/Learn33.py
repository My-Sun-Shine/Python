# 文件读写
with open('Learn/File/test01.txt', 'r') as f:
    # read()会一次性读取文件的全部内容，对大型文件不能这样使用
    # read(size) 每次最多读取size字节的内容
    # readline()每次读取一行，readlines()一次性读取全部内容，并返回list
    print(f.read())
print("——"*20)
with open('Learn/File/test01.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的\n去掉

# 二进制文件 图片 视频
with open("Learn/File/timg.jpg", "rb") as f:
    pass
    # 16进账的字节
    # print(f.read())

# 字符编码
# errors="ignore" 遇见错误编码如何处理，忽略
with open("Learn/File/test02.txt", "r", encoding="utf-8", errors="ignore") as f:
    print(f.read())

# w模式写入文件，如果文件已存在，则直接覆盖
# a模式为追加写入
with open("Learn/File/test01.txt", "w") as f:
    f.write("Hello,World\n")
    f.write("Hello,World\n")
    f.write("Hello,World\n")
