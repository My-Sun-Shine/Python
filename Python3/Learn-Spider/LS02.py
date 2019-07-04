#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/4 11:16
# @Author      ：Falling Stars
# @FileName    ：LS02
# @Software    ：PyCharm
# @Description ：使用urllib.error处理错误
from urllib import request, error


def DY_URLError():
    """URLError错误捕捉"""
    try:
        reponse = request.urlopen("http://cuiqingcai.com/index.html")
        print(reponse)
    except error.URLError as e:
        print(e.reason)


def DY_HTTPError():
    """
    HTTPError类，专门用来处理HTTP请求错误
    HTTPError类是URLError类的子类
    """
    try:
        reponse = request.urlopen("http://cuiqingcai.com/index.html")
        print(reponse)
    except error.HTTPError as e:
        # code:状态码，reson：错误原因，header：请求头
        print(e.reason, e.code, e.headers, sep="\n")


if __name__ == "__main__":
    # DY_URLError()
    DY_HTTPError()
