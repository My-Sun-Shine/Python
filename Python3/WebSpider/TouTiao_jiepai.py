#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/8 15:27
# @Author      ：Falling Stars
# @FileName    ：TouTiao_jiepai
# @Software    ：PyCharm
# @Description ：下载今日头条中的街拍图片
"""
https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1562571221550
https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1562571281760
"""

from urllib.parse import urlencode
import requests
import os
from hashlib import md5
from multiprocessing.pool import Pool


HEADERS = {
    'accept': 'application/json, text/javascript',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '__tasessionId=ipzixid1b1562570963234; csrftoken=f15b08c626c3b2dfd95098054adf966b; tt_webid=6711191121123722760; UM_distinctid=16bd07cceb2422-09ec538c4e4194-3e385c0c-100200-16bd07cceb3443; CNZZDATA1259612802=1920748031-1562569766-%7C1562569766; s_v_web_id=d082f371afa53f7977803142e8ef0f82',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

BASE_URL = os.path.abspath('jiepai')


def get_data(url, offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
        # 'timestamp': '1562571281760' # 时间戳
    }
    new_url = url + urlencode(params)
    try:
        response = requests.get(new_url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()  # 直接调取json方法将内容解析为Json返回
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_data(data):
    if data:
        items = data.get('data')
        if items:
            for item in items:
                title = item.get('title')
                images = item.get('image_list')
                if images:
                    for image in images:
                        yield {
                            'title': title,
                            'image': image.get('url')
                        }


def save_image(item):
    if not os.path.exists(BASE_URL):
        os.mkdir(BASE_URL)
    title = str(item.get('title')).replace('|', '')
    if not os.path.exists(os.path.join(BASE_URL, title)):
        os.mkdir(os.path.join(BASE_URL, title))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.jpg'.format(os.path.join(BASE_URL, title),
                                             md5(response.content).hexdigest())
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print("已经下载", file_path)
    except Exception as e:
        print("无法下载图片")


def main(offset):
    base_url = 'https://www.toutiao.com/api/search/content/?'
    data = get_data(base_url, offset)
    # print(data)
    jsons = parse_data(data)
    for item in jsons:
        save_image(item)


if __name__ == "__main__":
    pool = Pool()
    group = ([x * 20 for x in range(0, 3)])
    pool.map(main, group)
    pool.close()
    pool.join()
