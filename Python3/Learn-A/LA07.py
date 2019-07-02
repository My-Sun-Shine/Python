#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/2 18:05
# @Author      ：Falling Stars
# @FileName    ：LA07
# @Software    ：PyCharm
# @Description ：自定义一个复数类
from math import atan, hypot, sin, cos


class CustomComplex(object):
    def __init__(self, real, imag):
        """real 实部 imag 虚部"""
        self.real = real
        self.imag = imag

    def conjugate(self):
        """共轭复数"""
        return self.__class__(self.real, -self.imag)

    def argz(self):
        """复数的辅角"""
        return atan(self.imag / self.real)

    def __abs__(self):
        """绝对值"""
        return hypot(self.real, self.imag)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.real},{self.imag})"

    def __str__(self):
        return f"({self.real}{self.imag:+}j)"

    def __add__(self, other):
        """加法运算"""
        real_part = 0
        imag_part = 0
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real + other
            imag_part = self.imag
        if isinstance(other, CustomComplex):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag
        return CustomComplex(real_part, imag_part)

    def __sub__(self, other):
        """减法运算"""
        real_part = 0
        imag_part = 0
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real - other
            imag_part = self.imag
        if isinstance(other, CustomComplex):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag
        return CustomComplex(real_part, imag_part)

    def __mul__(self, other):
        """乘法运算"""
        real_part = 0
        imag_part = 0
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real * other
            imag_part = self.imag * other
        if isinstance(other, CustomComplex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + other.real * self.imag
        return CustomComplex(real_part, imag_part)

    __radd__ = __add__  # x+y==y+x
    __rmul__ = __mul__  # x*y==y*x

    def __rsub__(self, other):
        """x-y != y-x"""
        real_part = 0
        imag_part = 0
        if isinstance(other, float) or isinstance(other, int):
            real_part = other - self.real
            imag_part = -self.imag
        if isinstance(other, CustomComplex):
            real_part = other.real - self.real
            imag_part = other.imag - self.imag
        return CustomComplex(real_part, imag_part)

    def __eq__(self, other):
        """
        :param other: ==运算符
        :return:bool
        """
        return (self.real == other.real) and (self.imag == other.imag)

    def __ne__(self, other):
        """
        :param other: !=运算符
        :return:bool
        """
        return (self.real != other.real) or (self.imag != other.imag)

    def __pow__(self, power, modulo=None):
        """ **运算符 """
        r_raised = abs(self) ** power
        argz_multipied = self.argz() * power
        real_part = round(r_raised * cos(argz_multipied))
        imag_part = round(r_raised * sin(argz_multipied))
        return self.__class__(real_part, imag_part)


if __name__ == "__main__":
    cc1 = CustomComplex(1, 2)
    cc2 = CustomComplex(1, 2)
    print(cc1)  # 1+2j
    print(cc2)  # 1+2j
    cc1_copy = eval(repr(cc1))  # 使用eval、repr重建对象
    print(type(cc1_copy), cc1_copy.real, cc1_copy.imag)  # 1+2j
    print(cc1 + cc2)  # 2+4j
    print(cc1 - cc2)  # 0+0j
    print(cc1 + 5)  # 6+2j
    print(3 - cc2)  # 2-2j
    print(cc2 - 3)  # -2+2j
    print(cc1 * 6)  # 6+12j
    print(cc1 * (-6))  # -6-12j
    print(cc1 * cc2)  # -3+4j
    print(cc1 * CustomComplex(1, 3))  # -5+5j
    print(cc1 == CustomComplex(1, 2))  # True
    print(cc1 == cc2)  # True
    print(cc1 != cc2)  # False
    print(cc1 != CustomComplex(1, 3))  # True
    print(cc1 ** 2)  # -3+4j
    print(cc2 ** 5)  # 41-38j
