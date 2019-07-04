#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/4 14:52
# @Author      ：Falling Stars
# @FileName    ：LS05.py
# @Software    ：PyCharm
# @Description ：requests库的基本使用：get、post

import requests


def LS05_1():
    """
    示例
    :return:
    """
    r = requests.get("https://www.baidu.com")
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text)
    print(r.cookies)


def LS05_2():
    """
    requests的get请求
    :return:
    """
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) \
    #     Chrome/52.0.2743.116 Safari/537.36'
    # }
    # r = requests.get("https://www.zhihu.com/explore", headers=headers)
    # print(r.text)
    r = requests.get("https://github.com/favicon.ico")
    print(r.text)
    print(r.content)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


def LS05_3():
    """
    requests的post请求
    :return:
    """
    data = {'name': 'germey', 'age': '22'}
    r = requests.post("http://httpbin.org/post", data=data)
    print(r.text)


def LS05_4():
    r = requests.get('http://www.jianshu.com')
    print(type(r.status_code), r.status_code)
    print(type(r.headers), r.headers)
    print(type(r.cookies), r.cookies)
    print(type(r.url), r.url)
    print(type(r.history), r.history)


if __name__ == "__main__":
    # LS05_1()
    # LS05_2()
    # LS05_3()
    LS05_4()
