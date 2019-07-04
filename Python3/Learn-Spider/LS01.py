#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/3 17:34
# @Author      ：Falling Stars
# @FileName    ：LS01.py
# @Software    ：PyCharm
# @Description ：使用urllib.request的发送请求，带有参数、header、method、cookie

# urllib的模块
# 第一个request：它是最基本的HTTP请求模块，可以用它来模拟发送一请求，就像在浏览器里输入网址然后敲击回车一样，只需要给库方法传入URL还有额外的参数，就可以模拟实现这个过程
# 第二个error：模块即异常处理模块，如果出现请求错误，可以捕获这些异常，然后进行重试或其他操作保证程序不会意外终止
# 第三个parse：模块是一个工具模块，提供了许多 URL 处理方法，比如拆分、解析、合并等等的方法
# 第四个robotparser：主要是用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些网站不可以爬的，其实用的比较少
import urllib.request as request
import urllib.parse as parse
import http.cookiejar  # Cookie处理
import os.path


def LS01_1():
    # url = "https://www.python.org"
    url = "http://www.baidu.com/"
    response = request.urlopen(url)
    # print(response.read().decode("utf-8"))
    print(len(response.read().decode("utf-8")))
    print(type(response))  # 类型
    print(response.status)  # 响应码
    print(response.getheaders())  # 获取响应头
    print(response.getheader("Content-Type"))
    print("--" * 50)


def LS01_2():
    data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
    # http://httpbin.org/post，这个链接可以用来测试POST请求，它可以输出Request的一些信息，其中就包含传递的data参数
    url = 'http://httpbin.org/post'
    # urlopen方法其中还有timeout参数:设置超时时间，单位是秒，如果在设置时间内没有响应，则抛异常
    response = request.urlopen(url, data=data)
    print(response.read().decode("utf-8"))
    print("--" * 50)


def LS01_3():
    url = 'http://httpbin.org/get'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
    request_data = request.Request(url=url, data=data, headers=headers, method='POST')
    response3 = request.urlopen(request_data)
    print((response3.read().decode('utf-8')))
    print("--" * 50)


#
def LS01_4():
    """读取Cookie操作"""
    url = "http://www.baidu.com/"
    cookie = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open(url)
    for item in cookie:
        print(item.name, "=", item.value)
    print("--" * 50)


def LS01_5():
    """获取cookie并保存到txt文件中"""
    filename = 'cookies.txt'
    if os.path.exists(filename):
        os.remove(filename)
    url = "http://www.baidu.com/"
    # cookie = http.cookiejar.MozillaCookieJar(filename)
    cookie = http.cookiejar.LWPCookieJar(filename)  # LWP格式
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)


def LS01_6():
    """读取LWP格式,必须现有LWP格式的cookies文件"""
    filename = 'cookies.txt'
    url = "http://www.baidu.com/"
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open(url)
    print(response.read().decode("utf-8"))


if __name__ == "__main__":
    # LS01_1()
    # LS01_2()
    # LS01_3()
    # LS01_4()
    LS01_5()
    LS01_6()
