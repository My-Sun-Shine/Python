#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/16 16:25
# @Author      ：Falling Stars
# @FileName    ：urls
# @Software    ：PyCharm
# @Description ：
def china(start, end):
    for page in range(start, end + 1):
        yield 'http://tech.china.com/articles/index_' + str(page) + '.html'