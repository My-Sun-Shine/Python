#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        : 2019/6/30 21:53
# @Author      : MXW
# @FileName    : YouKu_DanMu.py
# @Software    : PyCharm
# @Description ：爬取网页版优酷《夏洛特烦恼》的弹幕数据并制作词云图
##########################################################################
# 首先，播放影片并打开Chrome开发者工具,选择Network。逐步拖动进度条并观察本地与服务器的请求规律
# 然后，确定弹幕数据来自JS实时加载而非XHR。需要注意的是，弹幕的请求数据不是规范的JSON格式
# 链接如下:
# https://service.danmu.youku.com/list?jsoncallback=jQuery111207324168796438026_1561804608754&mat=1&mcount=1&ct=1001&iid=349913820&aid=299162&cid=96&lid=0&ouid=0&_=1561804608770
# https://service.danmu.youku.com/list?jsoncallback=jQuery111207324168796438026_1561804608754&mat=2&mcount=1&ct=1001&iid=349913820&aid=299162&cid=96&lid=0&ouid=0&_=1561804608771
# https://service.danmu.youku.com/list?jsoncallback=jQuery111207324168796438026_1561804608754&mat=3&mcount=1&ct=1001&iid=349913820&aid=299162&cid=96&lid=0&ouid=0&_=1561804608775
# https://service.danmu.youku.com/list?jsoncallback=jQuery111207324168796438026_1561804608759&mat=0&mcount=1&ct=1001&iid=349913820&aid=299162&cid=96&lid=0&ouid=0&_=1561804608769
# 通过观察，发现只有mat这个变量不一样
from tqdm import tqdm
from requests.exceptions import RequestException
import requests
import os
import time

SAVE_DIR = "File/danmu.txt"
IMG_SHOW = "File/show01.jpg"
IMG_CLOUD = "File/cloud01.jpg"
FONT_TTF = "File/FZSTK.TTF"


def get_data(mat):
    url = 'https://service.danmu.youku.com/list'
    headers = {
        'Referer': 'https://v.youku.com/v_show/id_XMTM5OTY1NTI4MA==.html?spm=a2ha1.12701310.app.5~5!2~5!3~5~5~5!24~5~5~5~A',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    params = {
        'jsoncallback': 'jQuery111207324168796438026_1561804608754',
        'mat': mat,
        'mcount': '1',
        'ct': '1001',
        'iid': '349913820',
        'aid': '299162',
        'cid': '96',
        'lid': '0',
        'ouid': '0',
        # '_': '1561804608771'  # 提示：类似时间戳,去掉后不影响数据的获取
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            # print(response.text)
            # print(response.text[42:][:-2])

            dictinfo = eval(response.text[42:][:-2])  # 截取str，并把str转换为dict
            # print(type(dictinfo))
            # print(dictinfo["result"])

            with open(SAVE_DIR, 'a', encoding='utf-8') as f:
                for item in dictinfo["result"]:
                    f.write(item["content"] + '\n')
    except RequestException as e:
        print('Error: ', e.args)


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
    with open(SAVE_DIR, 'r', encoding='utf-8') as f:
        text = f.read()
    cut_text = " ".join(jieba.cut(text))
    color_mask = cv2.imread(IMG_SHOW)
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path=FONT_TTF,
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
    wCloud.to_file(IMG_CLOUD)

    plt.imshow(wCloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    if os.path.exists(SAVE_DIR):  # Determine whether storage path exists, no creation
        os.remove(SAVE_DIR)
    for i in tqdm(range(100), desc='抓取进度', ncols=100):
        get_data(str(i))
        time.sleep(1)
    show()
