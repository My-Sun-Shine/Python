
# -*- coding:utf-8 -*-

"""
@title: 爬取36kr的最新文章信息并保存至Mysql数据库，并把标题存储到txt文件中，并生成词云
@author:
"""

from tqdm import tqdm
from colorama import init, Fore
from fake_useragent import UserAgent
from requests.exceptions import RequestException
import requests
import mysql.connector
import time
import re

init(autoreset=True)
# 创建数据库链接
conn = mysql.connector.connect(
    user="root", password="123456", database="python3")


def get_one_page(page):
    """
    获取一页的最新文章JSON数据
    :param page: 页码
    :return: json
    """
    # 真实请求
    url = 'https://36kr.com/api/search-column/mainsite?per_page=20&page={}'.format(
        str(page))
    # 设置Headers
    headers = {
        'User-Agent': UserAgent().random,
        'Referer': 'https://36kr.com/',
        'Host': '36kr.com'
    }
    # 获取网页源代码
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            items = response.json()['data']['items']
            return items
        return None
    except RequestException:
        return None


def parse_one_page(items):
    """
    解析获取的JSON数据
    :param items: 获取的JSON数据段items
    :return: dict
    """
    # 存储单页总数据
    datas = list()
    for item in items:
        data = {
            # 文章ID
            'article_id': str(item['id']),
            # 标题
            'article_title': item['title'],
            # 类别
            'column_name': item['column_name'],
            # id
            'column_id': item['column_id'],
            # 封面图片链接
            'cover': item['cover'],
            # 发布时间
            'publish_time': item['published_at'],
            # 文章总结
            'summary': item['summary']
        }
        # 处理时间
        data['publish_time'] = re.search('(.*?)T(.*?)\+.*', data['publish_time']).group(
            1) + ' ' + re.search('(.*?)T(.*?)\+.*', data['publish_time']).group(2)
        # 存储
        datas.append(data)
        # 将标题写入文件.制作中文词云
        with open('WebSpider/File/36kr.txt', 'a', encoding='utf-8') as f:
            f.write(data['article_title']+"\n")
    return datas


def save_data(data):
    """
    存储数据至MySQL
    :param data: 解析的数据
    :return: None
    """
    dbName = "kr"
    data_dict = data[0]  # 获取集合的第一个字典

    # 获取(%s,%s,%s,%s,%s,%s,%s,%s)
    data_values = "("+"%s,"*(len(data_dict))+")"
    data_values = data_values.replace(",)", ")")

    # 获取要插入的字段
    dbField = data_dict.keys()
    dbField = str(tuple(dbField)).replace("'", "")

    # 拼接SQL语句字符串
    sql = "insert into %s %s values %s" % (dbName, dbField, data_values)
    # print(sql)

    # 把集合中的dict转换为tuple
    data_new = []
    for item in data:
        data_new.append(tuple(item.values()))

    cursor = conn.cursor()  # 获取游标
    # print(data_new)
    try:
        # 批量执行sql语句
        cursor.executemany(sql, data_new)
        conn.commit()
    except Exception as e:
        print(e)
        print(data)
        conn.rollback()
    finally:
        cursor.close()


def show():
    """
    根据文章标题,制作中文词云
    :return: None
    """
    from wordcloud import WordCloud
    import cv2
    import jieba
    import matplotlib.pyplot as plt
    # 文本
    with open('WebSpider/File/36kr.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    cut_text = " ".join(jieba.cut(text))
    color_mask = cv2.imread('WebSpider/File/show.jpg')
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path="WebSpider/File/FZSTK.TTF",
        # 设置背景色
        background_color='white',
        # 词云形状
        mask=color_mask,
        # 允许最大词汇
        max_words=2000,
        # 最大号字体
        max_font_size=40
    )
    wCloud = cloud.generate(cut_text)
    wCloud.to_file('WebSpider/File/cloud.jpg')

    plt.imshow(wCloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def main():
    """
    主函数
    :return: None
    """
    import os
    if os.path.exists("WebSpider/File/36kr.txt"):
        os.remove("WebSpider/File/36kr.txt")
    if os.path.exists("WebSpider/File/cloud.jpg"):
        os.remove("WebSpider/File/cloud.jpg")
    print(Fore.RED + '提示：截止目前的总数据量是77998条, 测试仅抓取前10页的共200条数据!\n')
    for i in tqdm(range(10),  desc='抓取进度', ncols=80):
        # 获取
        items = get_one_page(i+1)
        # 解析
        data = parse_one_page(items)
        # 保存
        save_data(data)
        time.sleep(1)
    show()


if __name__ == '__main__':
    main()
