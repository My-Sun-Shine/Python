#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time        ：2019/07/02 14:36:56
# @Author      ：My-Sun-Shine
# @File        ：LA06.py
# @Software    ：Visual Studio Code
# @Description ：重载内置运算符+ +=


class Order(object):
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __add__(self, other):
        """
        + 运算符 但只能 order+'FFF'
        """
        new_cart = self.cart.copy()  # 不能直接使用等于(如果使用等于则会改变原有list)，使用copy相当于拷贝一份，分成两份
        new_cart.append(other)
        return Order(new_cart, self.customer)

    def __iadd__(self, other):
        """+= 运算符"""
        self.cart.append(other)
        return self

    def __radd__(self, other):
        """+ 运算符 但只能 'FFF'+order """
        new_cart = self.cart.copy()  # 不能直接使用等于(如果使用等于则会改变原有list)，使用copy相当于拷贝一份，分成两份
        new_cart.insert(0, other)
        return Order(new_cart, self.customer)


order = Order(["A", "CC", "DD"], "ACCDD")
print((order + "FFF").cart)
print(order.cart)
print(("EEE" + order).cart)
print(order.cart)
order += "SSS"
print(order.cart)
print("----" * 30)
