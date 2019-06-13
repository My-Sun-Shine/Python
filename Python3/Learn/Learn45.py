# hashlib模块 提供常见的算法，MD5、SHA1
import random
import hashlib

# md5算法 就是生成固定的128字节的字符串，使用32位的16进制字符串表示
md5 = hashlib.md5()
md5.update("sadskdakdsa".encode("utf-8"))
print(md5.hexdigest())
md5 = hashlib.md5()
# 数据量较大时，可以多次调用
md5.update("sadskdakdsa".encode("utf-8"))
md5.update("sadskdakdsa".encode("utf-8"))
print(md5.hexdigest())

# SHA1和MD5类似，生成160字节，用40位的16进制字符串表示
sha1 = hashlib.sha1()
sha1.update("sadskdakdsa".encode("utf-8"))
sha1.update("sadskdakdsa".encode("utf-8"))
print(sha1.hexdigest())

###################################################################################


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    # 对密码处理，在密码后面加一个随机字符串 MD5(password + salt)
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)


print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))
print(not login('michael', '1234567'))
print(not login('bob', '123456'))
print(not login('alice', 'Alice2008'))
