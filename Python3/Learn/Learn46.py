# Hmac算法
import random
import hmac
message = b"Hello,world"
key = b"sssss"
h = hmac.new(key, message, digestmod="MD5")
print(h.hexdigest())


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))
print(not login('michael', '1234567'))
print(not login('bob', '123456'))
print(not login('alice', 'Alice2008'))