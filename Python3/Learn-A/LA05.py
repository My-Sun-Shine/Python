#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/2 14:00
# @Author      ：Falling Stars
# @FileName    ：LA05.py
# @Software    ：PyCharm
# @Description ：重载len、abs、str、repr、bool函数


class Order(object):
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        """重载len方法，返回值为一个整数值"""
        return len(self.cart)

    def __bool__(self):
        return len(self.cart) > 0


order = Order(["A", "CC", "DD"], "ACCDD")
print(len(order))  # 3
print(bool(order))  # True
print("---"*30)


class Vector(object):
    def __init__(self, x_comp, y_comp):
        self.x = x_comp
        self.y = y_comp

    def __abs__(self):
        """abs函数"""
        return (self.x * self.x + self.y * self.y) ** 0.5

    def __str__(self):
        return f'{self.x}i+{self.y}j'
    __repr__ = __str__


vector = Vector(-3, 3)
print(abs(vector))
print(str(vector))  # -3i+3j
print(repr(vector))  # -3i+3j
