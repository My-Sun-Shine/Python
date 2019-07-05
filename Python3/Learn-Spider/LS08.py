#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/4 17:38
# @Author      ：Falling Stars
# @FileName    ：LS08
# @Software    ：PyCharm
# @Description ：BeautifulSoup解析库的使用：节点选择器，方法选择器，CSS选择器
from bs4 import BeautifulSoup
import re


def LS08_1():
    """节点选择器"""
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    """
    string：获取节点的内容；attrs：获取节点的全部属性
    """
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())  # 把需要解析的字符串以标准缩进格式输出
    print('---' * 30)

    print(soup.title)  # title节点
    print(type(soup.title))
    print(soup.title.string)  # title节点的文本
    print(soup.title.name)  # title节点的name属性
    print('---' * 30)

    print(soup.head)  # 获取head节点
    print(soup.head.title.string)  # 获取head节点下的title节点的文本
    print('---' * 30)

    print(soup.p)  # 获取p节点，当有多个节点的时候，只返回第一个
    print(soup.p.attrs)  # 获取p节点的所有属性，字典类型
    print(soup.p.attrs['name'])  # 获取p节点的name属性，字符串
    print(soup.p["name"])  # 获取p节点的name属性，字符串
    print(soup.p["class"])  # 获取p节点的class属性，列表类型
    print(soup.p.string)  # 获取p节点的string


def LS08_2():
    """节点选择器"""
    html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
                and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
            <p class="story">...</p>
    """
    """
    contents：获取节点下的全部内容，返回list类型
    children：获取节点的全部直接子节点，返回一个生成器
    descendants：获取节点的全部子孙节点，返回一个生成器
    parent：获取节点的直接父节点，返回父节点的全部内容
    parents：获取节点的全部祖先节点，返回一个生成器
    next_sibling：获取节点的下一个兄弟元素
    previous_sibling：获取节点的上一个兄弟元素
    next_siblings：获取节点的后面所有的兄弟元素的生成器
    previous_siblings：获取节点的前面所有的兄弟元素的生成器
    """
    soup = BeautifulSoup(html, 'lxml')

    print(soup.p.contents)  # 获取p节点下的所有内容，列表类型返回
    print('---' * 30)

    print(soup.p.children)  # 获取所有子节点
    print('---' * 30)

    for i, child in enumerate(soup.p.children):
        print(i, child)  # 依次输出所有子节点
    print('---' * 30)
    print(soup.p.descendants)  # 获取所有子孙节点
    for i, child in enumerate(soup.p.descendants):
        print(i, child)
    print('---' * 30)

    print(soup.a.parent)  # 获取第一个a节点的直接父节点，返回的是父节点的全部内容
    print('---' * 30)

    print(list(enumerate(soup.a.parents)))  # 获取节点的全部祖先节点，返回一个生成器
    print('---' * 30)

    print("Next Sibling", soup.a.next_sibling)
    print("Prev Sibling", soup.a.previous_sibling)
    print("Next Sibling", list(enumerate(soup.a.next_siblings)))
    print("Prev Sibling", list(enumerate(soup.a.previous_siblings)))
    print('---' * 30)


def LS08_3():
    """
    方法选择器
    :return:
    """
    html = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
    """
    find_all(name , attrs , recursive , text ,limit, **kwargs)
    name：节点名；attrs：属性值；text：用来匹配节点的文本，传入的可以为字符串或正则表达式对象
    recursive：布尔型变量，是否递归，默认为True
    limit：范围限制参数，find函数即为limit参数值为1，限制寻找次数
    kwargs：选择具有指定属性的标签,是个冗余的参数，其可以被attributes等价代替
    find()：获取单个元素
    find_parents()：返回所有祖先节点 
    find_parent()：返回直接父节点
    find_next_siblings()：返回后面所有兄弟节点
    find_next_sibling()：返回后面第一个兄弟节点
    find_previous_siblings()：返回前面所有兄弟节点
    find_previous_sibling()：返回前面第一个兄弟节点
    find_all_next()：返回节点后所有符合条件的节点：
    find_next()：返回节点后第一个符合条件的节点
    find_all_previous()：返回节点前所有符合条件的节点, 
    find_previous()：返回节点前第一个符合条件的节点
    """
    soup = BeautifulSoup(html, 'lxml')

    # 通过标签名获取元素
    print(soup.find_all(name='ul'))  # 获取全部ul节点
    print(type(soup.find_all(name='ul')[0]))
    print('---' * 30)

    for ul in soup.find_all(name='ul'):
        print(ul.find_all(name='li'))
        for li in ul.find_all(name='li'):
            print(li.string)
    print('---' * 30)

    # 通过属性获取元素
    print(soup.find_all(attrs={'id': 'list-1'}))
    print(soup.find_all(attrs={'class': 'element'}))
    print(soup.find_all(id='list-1'))
    print(soup.find_all(class_='element'))  # class在Python是关键字，需要变为class_
    print('---' * 30)

    # text：用来匹配节点的文本，传入的可以为字符串或正则表达式对象
    print(soup.find_all(text='Foo'))  # 返回的是全部匹配的节点文本组成的列表
    print(soup.find_all(text=re.compile('Foo')))
    print('---' * 30)

    # find获取单个元素
    print(soup.find('ul'))  # 获取第一个ul节点
    print(type(soup.find('ul')))
    print(soup.find(class_='list'))  # 获取第一个ul节点


def LS08_4():
    """
    CSS 选择器
    """
    html = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
    """
    通过css选择器id class 标签名选取元素
    get_text()和string：获取文本
    ul['id'], ul.attrs['id'] 获取id属性
    """
    soup = BeautifulSoup(html, 'lxml')
    print(soup.select('.panel .panel-heading'))
    print('---' * 30)
    print(soup.select('.panel .panel-body .list'))  # 返回两个ul节点
    print('---' * 30)
    print(soup.select('ul li'))  # 获取全部的li节点
    print('---' * 30)
    print(soup.select('.panel .panel-body .list-small'))  # 返回第二个ul节点
    print('---' * 30)
    print(soup.select('#list-2 .element'))  # 获取id为list-2的节点下的class=element的所有节点
    print('---' * 30)

    # 嵌套选择
    # 获取ul节点下的li节点
    for ul in soup.select('ul'):
        print(ul.select('li'))
    print('---' * 30)

    # 获取属性
    for ul in soup.select('ul'):
        print(ul['id'], ul.attrs['id'])

    # 获取文本
    for li in soup.select('li'):
        print(li.get_text(), li.string)


if __name__ == "__main__":
    # LS08_1()
    # LS08_2()
    # LS08_3()
    LS08_4()
