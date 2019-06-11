#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import bs4
from bs4 import BeautifulSoup
print bs4

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

# 创建BeautifulSoup对象，第一个参数是HTML文档字符串，第二个参数HTML解析器，第三个参数HTML文档的编码
soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

print u"获取所有的链接"
links = soup.find_all("a")  # 获取所有的a节点
for item in links:
    print item.name, item["href"], item.get_text()

print "获取某个链接".decode("UTF-8").encode("GBK")
# 获取a节点中 href="http://example.com/elsie"的节点
link_node = soup.find("a", href="http://example.com/elsie")
# 获取节点的标签名称name，a节点的href属性，a节点的文本get_text()
print link_node.name, link_node["href"], link_node.get_text()

print u"正则匹配"
# 获取a标签中，href属性符合规定正则表达式的节点
link_node = soup.find("a", href=re.compile(r"ill"))
if link_node:
    print link_node.name, link_node["href"], link_node.get_text()

print u"获取p段落文字"
# class为关键字，需要改为class_
p_node = soup.find("p", class_="title")
if p_node:
    print p_node.name,  p_node.get_text()
