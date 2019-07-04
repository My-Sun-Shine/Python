#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/4 14:19
# @Author      ：Falling Stars
# @FileName    ：LS04.py
# @Software    ：PyCharm
# @Description ：分析Robots协议

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
print(rp.read())
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
