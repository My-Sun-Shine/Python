#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/4 11:27
# @Author      ：Falling Stars
# @FileName    ：LS03
# @Software    ：PyCharm
# @Description ：urllib.parse对URL地址的解析操作
from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin, urlencode, parse_qs, parse_qsl, quote, \
    unquote


def dy_urlparse():
    """
    urlparse 方法有三个参数，urlstring：待解析的URL，
    scheme：可选，协议(http、https)，它只有在urlstring中没有包括协议的时候才会有效
    allow_fragments：是否忽略fragment，默认为True，如果为False，则就会忽略，它就会被解析为path、params、query的一部分，fragment部分为空
    :return:
    """
    url = "http://www.baidu.com/index.html;user?#comment"
    result1 = urlparse(url)
    # (scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='', fragment='comment')
    print(type(result1), result1, sep="\n")
    print("---" * 30)

    result2 = urlparse(url, scheme="https", allow_fragments=False)
    # (scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='#comment', fragment='')
    print(type(result2), result2, sep="\n")


def dy_urlunparse():
    """
    urlunparse方法与urlparse相对立，接收一个可迭代对象，长度必须为6，返回链接
    :return:
    """
    data = ["http", "www.baidu.com", "index.html", "user", "a=6", "comment"]
    print(urlunparse(data))


def dy_urlsplit():
    """
    与urlparse方法差不多，但是params部分没有了，被合到path中了
    :return:
    """
    # SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='a=6', fragment='comment')
    result = urlsplit("http://www.baidu.com/index.html;user?a=6#comment")
    print(result)


def dy_urlunsplit():
    """
    urlunparse方法与urlunsplit差不多，接收一个可迭代对象，长度必须为5，返回链接
    :return:
    """
    data = ["http", "www.baidu.com", "index.html", "a=6", "comment"]
    # http://www.baidu.com/index.html?a=6#comment
    print(urlunsplit(data))


def dy_urljoin():
    """
    urljoin方法第一个参数为基础链接，第二个参数链接是经过分析出schema协议、netloc主机、path链接对第一个参数进行替换或补充
    :return:
    """
    print("---" * 30)
    print(urljoin('http://www.baidu.com', 'FAQ.html'))
    print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
    print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
    print(urljoin('http://www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com#comment', '?category=2'))
    print("---" * 30)


def dy_urlencode():
    """
    urlencode转换参数，构造get请求
    :return:
    """
    params = {
        'name': 'germey',
        'age': 22
    }
    base_url = "http://www.baidu.com?"
    url = base_url + urlencode(params)
    print(url)  # http://www.baidu.com?name=germey&age=22


def dy_parse_qs():
    """
    parse_qs把链接后面的get请求参数转换为字典
    :return:
    """
    url = "http://www.baidu.com?name=germey&age=22"
    query = url.split("?")[1]
    print(parse_qs(query))  # {'name': ['germey'], 'age': ['22']}


def dy_parse_qsl():
    """
    parse_qsl把链接后面的get请求参数转换为元组的列表，元组第一个参数为参数名，第二个为参数值
    :return:
    """
    url = "http://www.baidu.com?name=germey&age=22"
    query = url.split("?")[1]
    print(parse_qsl(query))  # [('name', 'germey'), ('age', '22')]


def dy_quote():
    """
    quote把内容转换为URL编码的格式
    :return:
    """
    keyword = "壁纸"
    url = "http://www.baidu.com?wd=" + quote(keyword)
    print(url)


def dy_unquote():
    """
    unquote把URL编码解析出来
    :return:
    """
    url = "http://www.baidu.com?wd=%E5%A3%81%E7%BA%B8"
    print(unquote(url))


if __name__ == "__main__":
    dy_urlparse()
    dy_urlunparse()
    dy_urlsplit()
    dy_urlunsplit()
    dy_urljoin()
    dy_urlencode()
    dy_parse_qs()
    dy_parse_qsl()
    dy_quote()
    dy_unquote()
