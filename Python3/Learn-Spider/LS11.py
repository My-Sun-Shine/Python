#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/9 13:33
# @Author      ：Falling Stars
# @FileName    ：LS11.py
# @Software    ：PyCharm
# @Description ：pytesseract库和tesserocr库识别验证码图片
import pytesseract
import tesserocr
from PIL import Image


def LS11_1():
    image = Image.open('./File/CheckCode.jpg')
    print(pytesseract.image_to_string(image))
    print(tesserocr.image_to_text(image))


def LS11_2():
    image = Image.open('./File/CheckCode.jpg')
    image_L = image.convert('L')  # 灰度化处理
    image_L.show()
    image_1 = image.convert('1')  # 二值化处理
    image_1.show()


def LS11_3():
    image = Image.open('./File/CheckCode.jpg')
    image = image.convert('L')  # 灰度化处理
    threshold = 150  # 二值化阀值
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    image.show()
    result = pytesseract.image_to_string(image)
    # 图片经过处理，答案更符合
    print(result)
    print(tesserocr.image_to_text(image))


if __name__ == '__main__':
    LS11_1()
    LS11_2()
    LS11_3()
