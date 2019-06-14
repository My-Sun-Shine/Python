# requests模块 操作URL资源
import requests
r = requests.get("https://www.douban.com/")
print(r.status_code)  # 状态
print(len(r.text))  # 文本

# 带参数
r1 = requests.get('https://www.douban.com/search',
                  params={'q': 'python', 'cat': '1001'})
print(r1.url)  # 链接
print(r1.encoding)  # 编码
# print(r1.content)

# 加入headers
r2 = requests.get("https://www.douban.com/", headers={
                  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(len(r2.text))

# 登录
r3 = requests.post("https://accounts.douban.com/login",
                   data={"from_email": "17862813319", "from_password": "db2019/"})
print(r3.status_code)
print(r3.headers)
print(r3.cookies)
