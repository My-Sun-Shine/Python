# 操作文件和目录，os模块
import time
import os
print("操作系统平台:", os.name)
# os.uname()#在window系统上不提供
print(os.environ)  # 环境变量
print(os.environ.get("PATH"))  # 获取某个环境变量
print(os.environ.get("x", "没有"))  # 设置查找某个环境变量，找不到的情况

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
print(os.path.abspath("."))  # 查看当前目录的绝对路径

# 把两个路径合成一个时，不要直接拼接字符串，要使用os.path.join
# window上得到C:\GitHub\Python\testdir，而Linux\Unix\Mac 得到C:\GitHub\Python/testdir
print(os.path.join("C:\GitHub\Python", "testdir"))

os.mkdir("C:/GitHub/Python/testdir")  # 创建目录
os.rmdir("C:/GitHub/Python/testdir")  # 删除目录

print(os.path.split("Learn\File\\timg.jpg"))  # 从路径中分出文件名
print(os.path.splitext("Learn\File\\timg.jpg"))  # 从路径中分出文件扩展名

# os.rename("", "")  # 重命名文件
# os.remove()

# 获取当前目录下的所有目录
print([x for x in os.listdir(".") if os.path.isdir(x)])
# 获取Learn目录下的所有.py文件
print([x for x in os.listdir("./Learn") if os.path.isfile("./Learn/" + x)
       and os.path.splitext(x)[1] == ".py"])


def findstrr(path, st):
    # 查找某个路径下的 文件名包括st的文件
    for x in os.listdir(path):  # 获取当前目录下的所有
        if os.path.isdir(x):
            new_path = os.path.join(path, x)
            findstrr(new_path, st)
        elif st in os.path.split(x)[1]:
            print("相关文件名：%s，相对路径：%s" % (x, os.path.relpath(path)))


path = os.path.abspath(".")  # 获取当前绝对路径
# print(path)
findstrr(path, "Learn")


def time_format(x):
    # return time.asctime(time.localtime(x))
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(x))


def cmd_dir():
    dir_and_file = [x for x in os.listdir(".")]
    gettimes = list(map(time_format, map(os.path.getmtime, dir_and_file)))
    getsize = list(map(os.path.getsize, dir_and_file))
    n = 0
    while n < len(dir_and_file):
        print(gettimes[n], "=>", str(getsize[n])+"bytes", "=>", dir_and_file[n])
        n += 1


cmd_dir()
