# -*- coding:utf-8 -*-

"""
@title: 使用urllib库爬取博客园文章，pyquery库分析文章，并存储至MySQL
@author: mxw
"""

from urllib import request, error, parse  # 下载HTML
from pyquery import PyQuery as pq  # 分析HTML
from tqdm import tqdm  # 进度条
from colorama import init, Fore  # 在控制台上可以输出颜色
import mysql.connector  # 数据库连接
import time  # 时间模块
import re  # 正则表达式


init(autoreset=True)  # 在window系统上输出颜色

# 创建数据库链接
conn = mysql.connector.connect(
    user="root", password="123456", database="python3")


def get_data(url, page):
    """
    获取博客园文章信息
    :return: HTTPResponse
    """
    _request = None
    if page:
        # 设置请求头
        headers = {
            'origin': 'https://www.cnblogs.com',
            'referer': 'https://www.cnblogs.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        # 设置请求参数
        payload = {
            'CategoryId': 808,
            'CategoryType': "SiteHome",
            'ItemListActionName': "PostList",
            'PageIndex': page,
            'ParentCategoryId': 0,
            'TotalPostCount': 4000,
        }
        # 编码
        data = bytes(parse.urlencode(payload), encoding='utf-8')
        # 构建Request类
        _request = request.Request(
            url=url, headers=headers, data=data, method='POST')
    else:
        _request = request.Request(url=url)
    try:
        response = request.urlopen(_request)
        if response.status == 200:
            return response
    except error.HTTPError as e:
        print(e.reason, e.code, sep='\n')
        return None
    except error.URLError as e:
        print(e.reason)
        return None


def parse_data(response):
    """
    解析数据
    :param response: HTTPResponse
    :return: None
    """
    # 获取网页源代码
    html = response.read().decode('utf-8')
    doc = pq(html)
    # 获取包含文章信息的div节点
    divs = doc('.post_item').items()
    # 存储列表
    data = []
    for div in divs:
        # print("——"*30)
        _data = {
            # 文章标题
            "title": div.find(".titlelnk").text(),
            # 文章详情页链接
            'url': div.find(".titlelnk").attr("href"),
            # 文章简介
            'short': div.find(".post_item_summary").text(),
            # 博主
            'author': div.find(".post_item_foot .lightblue").text(),
            # 博主的主页链接
            'author_url': div.find(".post_item_foot .lightblue").attr("href"),
            # 发布时间
            'create_time': re.search("\d{4}-\d{2}-\d{2} \d{2}:\d{2}", div.find(".post_item_foot").text()).group(),
            # 评论数
            # \D代表非数字
            'comment_counts': re.sub("\D", '', div.find(".article_comment .gray").text()),
            # 阅读量
            'read_counts': re.sub("\D", '', div.find(".article_view .gray").text()),
        }

        # print(_data)
        data.append(_data)
    # print(len(html))
    return data


def save_data(data):
    """
    存储数据至MySQL
    :param data: 解析的数据
    :return: None
    """
    dbName = "cnblogs"
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


def main(url, page=''):
    """
    主函数
    :param url: 访问链接
    :return: None
    """
    # 获取数据
    response = get_data(url, page)
    # 解析数据
    data = parse_data(response)
    # 存储数据
    save_data(data)


if __name__ == '__main__':
    # 红色输出
    print(Fore.RED + '提示：本次抓取范围仅限博客园最新文章, 测试仅抓取前10页数据！\n')
    url = 'https://www.cnblogs.com/'
    for i in tqdm(range(10), desc='抓取进度', ncols=100):
        main(url, i+1)
        time.sleep(1)
    conn.close()
