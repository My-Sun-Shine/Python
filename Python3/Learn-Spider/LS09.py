#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/5 13:48
# @Author      ：Falling Stars
# @FileName    ：LS09.py
# @Software    ：PyCharm
# @Description ：PyQuery库的操作：CSS选择器，伪类选择器，节点操作
from pyquery import PyQuery as pq
import requests


def LS09_1():
    """
    PyQuery中可以直接传入URL，效果与传入通过URL获取的HTML源码一样
    doc = pq(filename='demo.html') 还可以获取文件
    """
    doc = pq(url='http://cuiqingcai.com')
    print(doc('title'))

    doc = pq(requests.get('http://cuiqingcai.com').text)
    print(doc('title'))


HTML = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''


def LS09_2():
    """
    CSS选择器
    :return:
    find()：查找的节点的所有子孙节点，传入参数为CSS选择器
    children()：查找的节点的所有子节点，传入参数为CSS选择器
    parent()：查找节点的直接父节点，传入参数为CSS选择器
    parents()：查找节点的祖先节点，传入参数为CSS选择器
    siblings()：查找节点的兄弟节点，传入参数为CSS选择器
    items()：获取符合条件的生成器，传入参数为CSS选择器
    attr()：获取属性
    text()：获取文本
    html()：获取html代码
    """
    doc = pq(HTML)
    print(doc('#container .list li'))
    print(type(doc('#container .list li')))
    print('---' * 30)

    # 获取子节点 find()
    lis = doc('.list').find('li')  # 获取class=list的节点下的li
    print(type(lis))
    print(lis)
    print('---' * 30)
    print(doc('.list').children('.active'))  # 获取符合的子节点
    print('---' * 30)

    # 获取父节点
    print(doc('.item-0.active').parent())  # 获取直接父节点
    print('---' * 30)
    print(doc('.item-0.active').parents())  # 获取祖先节点
    print('---' * 30)

    # 获取兄弟节点
    print(doc('.item-0.active').siblings())
    print('---' * 30)

    # 遍历
    for li in doc('li').items():
        print(li)
    print('---' * 30)

    print(doc(".item-0.active a").attr('href'))  # 获取属性
    print(doc(".item-0.active a").attr.href)
    print(doc(".item-0.active a").text())  # 文本
    print(doc(".item-0.active a").html())  # HTML


def LS09_3():
    """
    节点操作
    :return:
    remove_class()：移除class
    add_class()：添加class
    attr()：方法来修改属性，第一个参数为属性名，第二个参数为属性值
    text() 和 html() 方法来改变节点内部的内容
    
    attr()方法如果只传入第一个参数属性名，则是获取这个属性值，如果传入第二个参数，可以用来修改属性值，
    text()和html()方法如果不传参数是获取节点内纯文本和HTML文本，如果传入参数则是进行赋值
    remove()：删除节点
    append()、empty()、prepend()等方法，和jQuery的用法是完全一致的，http://pyquery.readthedocs.io/en/latest/api.html
    修改节点会影响原本的PyQuery对象
    """
    doc = pq(HTML)

    li = doc('.item-0.active')
    print(li)
    li.remove_class('active')  # 移除class
    print(li)
    li.add_class('active')  # 添加class
    print(li)
    print('---' * 30)

    li = doc('.item-0.active')
    print(li)
    li.attr('name', 'link')  # 修改属性
    print(li)
    li.text('changed item')  # 修改节点内容
    print(li)
    li.html('<span>changed item</span>')  # 修改节点内容
    print(li)
    print('---' * 30)

    li = doc('.item-1.active')
    print(li.html())
    li.find('a').remove()
    print(li.html())


def LS09_4():
    """
    伪类选择器
    """
    doc = pq(HTML)
    li = doc('li:first-child')  # 获取第一个li节点
    print(li)
    li = doc('li:last-child')  # 获取最后一个li节点
    print(li)
    li = doc('li:nth-child(2)')  # 获取第二个li节点
    print(li)
    li = doc('li:gt(2)')  # 第三个 li 之后的 li 节点
    print(li)
    li = doc('li:nth-child(2n)')  # 偶数位置的 li 节点
    print(li)
    li = doc('li:contains(second)')  # 包含 second 文本的 li 节点
    print(li)


if __name__ == '__main__':
    # LS09_1()
    # LS09_2()
    # LS09_3()
    LS09_4()
