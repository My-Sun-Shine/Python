#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import cookielib

url = "http://www.baidu.com/"

print("----"*20)
response = urllib2.urlopen(url)  # 直接请求
print(response.getcode())  # 获取状态码，200
content = response.read()  # 读取内容
print(len(content))

print("----"*20)
# 添加data、 http header
request = urllib2.Request(url)
request.add_header("User-Agent", "Mozilla/5.0")  # 伪造为浏览器
response = urllib2.urlopen(request)
print(response.getcode())
content = response.read()  # 读取内容
print(len(content))

print("----"*20)
cj = cookielib.CookieJar()  # 创建Cookie容器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  # 创建1个opener
urllib2.install_opener(opener)  # 给urllib安装opener
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print len(response3.read())
