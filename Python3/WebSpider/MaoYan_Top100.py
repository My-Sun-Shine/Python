# -*- coding:utf-8 -*-
"""
@title: Spider Maoyan Top100
@author: 
"""

import requests  # 请求UL资源
import re  # 正则表达式
import json  # JSON
from requests.exceptions import RequestException
from pyquery import PyQuery as pq  # 分析HTML
import time
import os


def get_one_page(url):
    """
    获取每页的网页源代码
    :param url: 请求链接
    :return: 网页的文本内容
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def pyquery_one_page(html):
    """
    使用pyquery解析网页数据
    :param html: 网页的文本内容
    :return: 字典
    """
    data = []
    doc = pq(html)
    dds = doc('dd').items()
    for dd in dds:
        # print(dd)
        # print("——"*30)
        _dd = {
            'index': dd.find(".board-index").text(),
            'image': dd.find(".board-img").attr("src") if dd.find(".board-img").attr("src") else dd.find(".board-img").attr("data-src"),
            'title': dd.find(".movie-item-info .name").text(),
            'actor': dd.find(".movie-item-info .star").text()[3:],
            'time': dd.find(".movie-item-info .releasetime").text()[5:],
            'score': dd.find(".integer").text()+dd.find(".fraction").text()
        }
        data.append(_dd)
        # print(_dd)
    return data


def parse_one_page(html):
    """
    使用正则表达式解析网页数据
    :param html: 网页的文本内容
    :return: 字典
    """
    pattern = re.compile(
        r'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.'
        r'*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1].split('@')[0],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def write_to_file(content):

    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset={}'.format(str(offset))
    html = get_one_page(url)
    for item in pyquery_one_page(html):
        write_to_file(item)


if __name__ == '__main__':
    if os.path.exists("result.txt"):
        os.remove("result.txt")
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
