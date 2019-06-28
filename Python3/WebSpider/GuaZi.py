# -*- coding:utf-8 -*-

"""
@title: requests+BeautifulSoup抓取瓜子二手车五个城市的数据，共1万条数据，保存到csv文件
@author: mxw
"""

import requests
from bs4 import BeautifulSoup  # 分析HTML
from tqdm import tqdm  # 进度条
from colorama import init, Fore  # 在控制台上可以输出颜色
import csv
import time  # 时间模块

init(autoreset=True)  # 在window系统上输出颜色

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'uuid=6c659f65-68d3-4101-c593-45f9d2ee8c36; antipas=51908107j8R52M4018A232599Fq6U; ganji_uuid=8945426125336121391710; lg=1; sessionid=9afce447-384b-4561-9396-0be9352a3c99; cityDomain=hz; clueSourceCode=10103000312%2300; user_city_id=26; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%2520%25e4%25ba%258c%25e6%2589%258b%25e8%25bd%25a6%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%226c659f65-68d3-4101-c593-45f9d2ee8c36%22%2C%22sessionid%22%3A%229afce447-384b-4561-9396-0be9352a3c99%22%7D; preTime=%7B%22last%22%3A1561704793%2C%22this%22%3A1561689317%2C%22pre%22%3A1561689317%7D',
    'Host': 'www.guazi.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

FIELDNAMES = ['city', 'name', 'img', 'detail', 'time', 'mileage',
              'type', 'price', 'old-price', 'icon-new', 'label']  # 标题名称

CITYS = {"bj": "北京", "sh": "上海", "sz": "深圳", "gz": "广州", "hz": "杭州"}


def get_data(url):
    try:
        req = requests.get(url, headers=HEADERS)
        req.encoding = 'utf-8'
        if req.status_code == 200:
            return req.text
    except Exception as e:
        print(e)
        return None


def parse_data(html, city):
    doc = BeautifulSoup(html, "html.parser")
    ul = doc.find('ul', class_="carlist clearfix js-top")
    li_list = ul.find_all('li')
    data = []
    for li in li_list:
        str1 = li.find('div', class_="t-i").get_text()
        str_list = str1.split("|")
        labels = li.find('div', class_="t-price").find_all('i')
        _data = {
            # 城市
            "city": city,
            # 车名
            'name': li.find('a', class_="car-a")["title"],
            # 图片链接
            'img': li.img['src'].split('@')[0] if 'src' in li.img.attrs.keys() else li.img['data-src'].split('@')[0],
            # 详情链接
            'detail': li.find('a', class_="car-a")["href"].split('#')[0],
            # 上牌年份
            'time': str_list[0],
            # 表显里程
            'mileage': str_list[1] if len(str_list) > 1 else '',
            # 类型
            'type': str_list[2] if len(str_list) > 2 else '',
            # 价格
            'price': li.find('div', class_="t-price").p.get_text(),
            # 以前的价格
            'old-price': li.find('em', class_='line-through').get_text() if li.find('em', class_='line-through') != None else '',
            # 是否新上架
            'icon-new': '新上架' if li.find('em', class_="icon-new") != None else '',
            # 标签
            "label": ','.join(label.get_text() for label in labels) if labels != None else ''
        }
        data.append(_data)
    return data


def save_csv(data_list, fieldnames):
    # a模式追加
    with open('data.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for data in data_list:
            writer.writerow(data)


def init_csv(fieldnames):
    # w模式，新建写入
    with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # 先写入头信息


def main(url, city):
    # 获取数据
    html = get_data(url)
    # 解析数据
    data = parse_data(html, city)
    # 保存数据
    save_csv(data, FIELDNAMES)


if __name__ == '__main__':
    # 初始化csv文件
    init_csv(FIELDNAMES)
    # 红色输出
    for k, v in CITYS.items():
        print(Fore.RED + '提示：正在抓取%s瓜子二手车数据！\n' % v)
        for i in tqdm(range(50), desc='抓取进度', ncols=60):
            url = 'https://www.guazi.com/%s/buy/%s' % (k, 'o'+str(i))
            main(url, v)
            time.sleep(1)
