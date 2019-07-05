#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/4 16:11
# @Author      ：Falling Stars
# @FileName    ：LS07
# @Software    ：PyCharm
# @Description ：XPath的使用，即lxml库，通过XPath获取元素节点
from lxml import etree

"""
常用规则：nodename：获取该节点的所有子节点；/：从当前节点选取直接子节点；//：从当前节点选取子孙节点
.：选取当前节点；..：选取当前节点的父节点；@：选取属性
//title[@lang=’eng’]
这就是一个 XPath 规则，它就代表选择所有名称为 title，同时属性 lang 的值为 eng 的节点
"""


def LS07_1():
    text = '''
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a>
        </ul>
    </div>
    '''
    html = etree.HTML(text)
    result = etree.tostring(html)
    print(result.decode('utf-8'))


def LS07_2():
    html = etree.parse("File/Test.html", etree.HTMLParser())
    # print(etree.tostring(html).decode('utf-8'))
    print(html.xpath('//*'))
    print(html.xpath('//li'))  # 获取li节点
    print(html.xpath('//li/a'))  # 获取li节点的子节点a
    print(html.xpath('//ul//a'))  # 获取ul下的子孙a节点
    print("---" * 30)
    print(html.xpath('//a[@href="link4.html"]/../@class'))  # 先得到a节点，取a的父节点的class
    print(html.xpath('//a[@href="link4.html"]/parent::*/@class'))  # parent::获取父节点
    print("---" * 30)
    print(html.xpath('//li[@class="item-0"]'))  # 获取class为item-0的li节点
    print("---" * 30)
    print(html.xpath('//li[@class="item-0"]/text()'))  # 获取class为item-0的li节点，获取的文本是li下的文本
    print(html.xpath('//li[@class="item-0"]/a/text()'))  # 获取class为item-0的li节点，文本获取的是a节点的
    print(html.xpath('//li[@class="item-0"]//text()'))  # 获取class为item-0的li节点，文本获取的是a节点的+li节点的
    print("---" * 30)
    print(html.xpath('//li/a/@href'))
    print("---" * 30)
    print(html.xpath('//li[1]/a/text()'))  # 获取第一个li节点下的a节点的文本
    print(html.xpath('//li[last()]/a/text()'))  # 最后一个li节点
    print(html.xpath('//li[position()<3]/a/text()'))  # 第一个第二个li节点
    print(html.xpath('//li[last()-2]/a/text()'))  # 倒数第三个li节点
    print("---" * 30)
    # XPath Axes（轴）
    # ancestor轴：         可以获取所有祖先节点，其后需要跟两个冒号
    # attribute轴：        可以获取所有属性值
    # child轴：            可以获取所有直接子节点
    # descendant轴：       可以获取所有子孙节点
    # following轴：        可以获取当前节点之后的所有节点
    # following-sibling轴：可以获取当前节点之后的所有同级节点
    print(html.xpath('//li[1]/ancestor::*'))  # 获取第一个li节点的所有祖先节点
    print(html.xpath('//li[1]/ancestor::div'))  # 获取第一个li节点的所有祖先节点中的div节点
    print(html.xpath('//li[1]/attribute::*'))  # 获取li节点的所有属性值
    print(html.xpath('//li[1]/child::a[@href="link1.html"]'))  # 获取所有直接子节点，且href为link1.html的
    print(html.xpath('//li[1]/descendant::span'))  # 获取所有子孙节点中span节点
    print(html.xpath('//li[1]/following::*[2]'))  # 获取当前节点之后的所有节点下的第二个
    print(html.xpath('//li[1]/following-sibling::*'))  # 获取当前节点之后的所有同级节点


def LS07_3():
    """属性多值匹配和多属性匹配"""
    text = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text)
    print(html.xpath('//li[@class="li"]/a/text()'))
    print(html.xpath('//li[contains(@class,"li")]/a/text()'))  # 属性多值匹配
    print(html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()'))  # 多属性匹配


if __name__ == "__main__":
    # LS07_1()
    LS07_2()
    # LS07_3()
