#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '  # 模块的文档注释

__author__ = 'Michael Liao'  # 作者
# 第一行可以让这个py文件直接在Unix/Linux/Mac上运行
# 第二行表示该文件本身是有UTF-8编码
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
    
def _private_1():
    print("私有方法")

# 如果该程序文件是主程序时__name__为__main__，反之当该模块被其他模块引用时，__name__则不是
if __name__ == '__main__':
    test()

# 模块名要遵循Python变量命名规范，不要使用中文和特殊字符
# 模块名不要和系统模块名冲突
# 类似于像__name__这样的变量，都是系统的特殊变量
# 类似于_xxx和__xxx这样的函数和变量，默认是私有的，因为在Python中没有一种方法可以完全限制访问私有函数或变量，但是，从编程习惯上可以不去引用
