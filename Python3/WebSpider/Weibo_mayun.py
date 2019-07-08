#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/8 12:59
# @Author      ：Falling Stars
# @FileName    ：Weibo_mayun
# @Software    ：PyCharm
# @Description ：爬取马云的微博信息，保存到JSON文件中
"""
微博是Ajax请求，就是Network面板中的xhr请求，请求地址https://m.weibo.cn/u/2145291155
https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155
https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155&page=2
https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155&page=3
"""
from urllib.parse import urlencode
from tqdm import tqdm
from colorama import init, Fore  # 在控制台上可以输出颜色
import requests
from pyquery import PyQuery as pq
import time  # 时间模块
import json
import os

HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'MWeibo-Pwa': '1',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

SAVE_URL = 'weibo_mayun.json'
LAST_PAGE = False  # 是否是最后一页
init(autoreset=True)  # 在window系统上输出颜色


def get_data(url, page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }
    new_url = url + urlencode(params)
    try:
        response = requests.get(new_url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()  # 直接调取json方法将内容解析为Json返回
    except requests.ConnectionError as e:
        print('Error', e.args)


def get_page(url, page):
    """
    获取页数
    :param url:链接
    :param page: 第几页
    :return:
    """
    page_size = 10  # 每页10个
    data = get_data(url, page)
    if data:
        try:
            # 总条数
            total_count = data.get('data').get('cardlistInfo').get('total')
            # 总页数
            page_count = total_count // page_size + (0 if total_count % page_size == 0 else 1)
            return page_count
        except Exception as e:
            print(e.args)
            return 0
    return 0


def parse_data(data):
    if data:
        new_data = []
        items = data.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {
                'id': item.get('id'),
                'text': pq(item.get('text')).text(),
                'attitudes': item.get('attitudes_count'),  # 点赞
                'comments': item.get('comments_count'),  # 评论
                'reposts': item.get('reposts_count')  # 转发
            }
            new_data.append(weibo)
        return new_data


def save_data_json(data, notlast):
    if os.path.exists(SAVE_URL):
        with open(SAVE_URL, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=2, ensure_ascii=False))
            if notlast:  # 最后一页的最后一条不添加，
                f.write(',')


def main(url, page):
    data = get_data(url, page)
    new_data = parse_data(data)
    for j in range(len(new_data)):
        if LAST_PAGE:  # 最后一页
            if j + 1 == len(new_data):  # 最后一条
                save_data_json(new_data[j], False)
                break
        save_data_json(new_data[j], True)


if __name__ == "__main__":
    if os.path.exists(SAVE_URL):
        os.remove(SAVE_URL)
    course = open(SAVE_URL, 'w', encoding='utf8')
    course.write('[')
    course.close()

    print(Fore.RED + '提示：本次抓取范围是马云的个人微博！\n')
    base_url = 'https://m.weibo.cn/api/container/getIndex?'
    count = get_page(base_url, 1)
    if count != 0:
        for i in tqdm(range(count), desc='抓取进度', ncols=100):
            if i + 1 == count:  # 判断是否为最后一页
                LAST_PAGE = True
            main(base_url, i + 1)
            time.sleep(1)
    course = open(SAVE_URL, 'a+', encoding='utf8')
    course.write(']')
    course.close()
