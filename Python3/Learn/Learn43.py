# Base64模块，使用64个字符表示任意二进制数据的方法
# Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%
# 好处是编码后的文本数据可以在邮件正文、网页等直接显示
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节,Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉
import base64
str1 = b"binary\x00string"
str2 = b'YmluYXJ5AHN0cmluZw=='
str3 = b'MJUW4YLSPEAHG5DSNFXGO==='
# 编码对象的位数要是3的倍数（最终编码对象位数要能被6整除）
# 解码对象的位数要是4的倍数（最终解码对象要能被8整除）
print(len(str1))
print(len(str2))
print(len(str3))
print(base64.b64encode(str1))

print(base64.b64decode(str2))

print(base64.b32encode(str1))
print(base64.b32decode(str3))

print("由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种'url safe'的base64编码，其实就是把字符+和/分别变成-和_")
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
