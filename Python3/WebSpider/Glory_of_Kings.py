"""
@title: 王者荣耀皮肤下载
@author:
"""

import urllib
import requests
import os
from colorama import init, Fore  # 在控制台上可以输出颜色


def saveImg(skin_url, save_file_name):
    try:
        # 使用urllib.request
        # urllib.request.urlretrieve(skin_url, filename=save_file_name)

        # 使用requests下载
        # 获取图片的位数据(二进制流数据)
        response_skin_content = requests.get(skin_url).content
        # 保存图片
        with open(save_file_name, 'wb') as f:
            f.write(response_skin_content)

        return True
    except Exception as e:
        return False


init(autoreset=True)  # 在window系统上输出颜色
# 全英雄列表请求链接
herolist_url = 'https://pvp.qq.com/web201605/js/herolist.json'
# 获取数据
response = requests.get(herolist_url).json()

# 根据英雄的皮肤链接，分析并下载英雄的皮肤
save_dir = os.path.join(os.path.abspath("."), "img")  # 指定下载位置
print(save_dir)
if not os.path.exists(save_dir):
    os.mkdir(save_dir)  # 创建文件夹

for i in range(len(response)):
    # print(response[i])
    # 下载当前英雄的所有皮肤
    hero_num = response[i]['ename']     # 英雄序号
    hero_name = response[i]['cname']    # 英雄名称
    print(response[i].keys())
    if "skin_name" in response[i].keys():
        # 获取英雄皮肤列表
        skin_names = response[i]['skin_name'].split('|')
        for cnt in range(len(skin_names)):
            skin_name = skin_names[cnt]         # 皮肤名称
            save_file_name = save_dir + "\\" + \
                str(hero_num) + '-' + hero_name + '-' + skin_name + '.jpg'
            # print(save_file_name)
            # skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(
            #     hero_num, hero_num, str(cnt+1))
            skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%s/%s-bigskin-%s.jpg' % (
                hero_num, hero_num, str(cnt+1))
            print(skin_url)
            if saveImg(skin_url, save_file_name):
                print(str(hero_num) + '-' + hero_name +
                      '-' + skin_name + '.jpg', "下载完成")
            else:
                print(Fore.RED + str(hero_num) + '-' + hero_name +
                      '-' + skin_name + '.jpg', Fore.RED + "下载失败")
    else:
        print(Fore.RED + str(hero_num) + '-' +
              hero_name + '.jpg', Fore.RED + "下载失败")
