# 正则表达式
# \d匹配一个数字，\w匹配一个字母或者数字, .匹配任意字符，\s匹配一个空格
# *表示任意个字符包括0个，+表示至少一个字符，?表示0个或1个字符，{n}表示n个字符，{n,m}表示n-m个字符
# 使用\对特殊字符进行转义，比如"-","_"字符
# A|B可以匹配A或者B
# ^表示行的开头，^\d表示数字开头
# $表示行的结束，\d$表示数字结束
# re模块
import re

# match方法判断是否匹配，成功返回match对象，失败返回None
print(re.match(r"\d{3}\-\d{3,8}$", '010-2563'))
print(re.match(r"\d{3}\-\d{3,8}$", '010 2563'))

# 切割字符串
str1 = "a b   c"
print(str1.split(" "))  # 使用空格分隔
print(re.split(r"\s+", str1))  # 使用re模块
str2 = "a b, c   d"
print(re.split(r"[\s\,]+", str2))

# 分组，使用()表示要提取的分组
m = re.match(r"(\d{3})\-(\d{3,8})$", '010-2563')
# group(0)永远是原始字符串
print(m.group(0), m.group(1), m.group(2))


# 贪婪匹配
# \d+采用贪婪匹配，会把后面的0全部匹配上，这样0*就是空了
# \d+?是非贪婪匹配
print(re.match(r"^(\d+)(0*)$", "402000").groups())
print(re.match(r"^(\d+?)(0*)$", "402000").groups())
