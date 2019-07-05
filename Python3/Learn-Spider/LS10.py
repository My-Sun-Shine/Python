#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/5 16:28
# @Author      ：Falling Stars
# @FileName    ：LA10
# @Software    ：PyCharm
# @Description ：
import requests
from pyquery import PyQuery as pq

URL = 'https://www.zhihu.com/explore'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/58.0.3029.110 Safari/537.36'
}


def get_data(url, headers):
    rep = requests.get(url, headers=headers)
    html = rep.text
    doc = pq(html)
    items = doc('.explore-tab .feed-item').items()
    all_data = []
    for item in items:
        _data = {
            "question": item.find('.question_link').text(),
            'author': item.find('.author-link-line').text(),
            'answer': pq(item.find('.content').html()).text()
        }
        all_data.append(_data)
    return all_data


def save_data_txt(datas):
    """
    保存数据到txt中
    :param datas:
    :return:
    """
    with open('explore.txt', 'w', encoding='utf-8') as f:
        for item in datas:
            f.write('\n'.join([item['question'], item['author'], item['answer']]))
            f.write('\n' + '=====' * 50 + '\n')


if __name__ == "__main__":
    data = get_data(URL, HEADERS)
    save_data_txt(data)
