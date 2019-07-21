#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/5 16:28
# @Author      ：Falling Stars
# @FileName    ：LA10
# @Software    ：PyCharm
# @Description ：
import requests
import json
import csv
from pyquery import PyQuery as pq

URL = 'https://www.zhihu.com/explore'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/58.0.3029.110 Safari/537.36',
    'host': 'www.zhihu.com'
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
    保存数据到txt文件
    :param datas:
    :return:
    """
    with open('explore.txt', 'w', encoding='utf-8') as f:
        for item in datas:
            f.write('\n'.join([item['question'], item['author'], item['answer']]))
            f.write('\n' + '=====' * 50 + '\n')


def save_data_json(datas):
    """
    保存数据到json文件
    :param datas:
    :return:
          python对象<--->JSON字符串
                dict<-->object
          list,tuple<-->array
        str, unicode<-->string
    int, long, float<-->number
                True<-->true
               False<-->false
                None<-->null
    loads():将已编码的JSON字符串解码为Python对象
    dumps():将Python对象编码成JSON字符串，参数indent:代表缩进字符个数，参数ensure_ascii:为False才可正常写入中文
    load(f)：参数f为文件对象，读取json文件数据，转成Python对象
    dump(data,f)：将Python对象转化成json数据后写入json文件，参数f为文件对象，参数data为数据
    """
    # print(" ".join(datas)) 会报错TypeError: sequence item 0: expected str instance, dict found
    # data_str = " ".join('%s' % data for data in datas)
    with open('json.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(datas, indent=2, ensure_ascii=False))


def save_data_csv(datas):
    """
    保存数据到csv文件
    :param datas:
    :return:
    """
    with open('data.csv', 'w', encoding='utf-8') as csvfile:
        data_dict = datas[0]  # 获取集合的第一个字典
        dbField = data_dict.keys()  # 获取标题
        writer = csv.DictWriter(csvfile, fieldnames=dbField)
        writer.writeheader()  # 输入标题
        # writer.writerows(datas)
        for item in datas:
            writer.writerow(item)


if __name__ == "__main__":
    data = get_data(URL, HEADERS)
    # save_data_txt(data)
    # save_data_json(data)
    save_data_csv(data)
