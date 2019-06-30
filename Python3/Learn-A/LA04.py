#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/2 13:37
# @Author      ：Falling Stars
# @FileName    ：LA04
# @Software    ：PyCharm
# @Description ：Python里面没有常量关键字，自定义一个常量类
import sys


class Const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s) " % name)
        self.__dict__[name] = value


sys.modules[__name__] = Const()

# 在其他py文件中进行调用会报错
# import LA04
#
# LA04.magic = 1
# LA04.magic = 1
