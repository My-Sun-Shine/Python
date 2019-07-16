#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/16 16:27
# @Author      ：Falling Stars
# @FileName    ：run
# @Software    ：PyCharm
# @Description ：
import sys
from scrapy.utils.project import get_project_settings
from Scrapy_crawl.spiders.universal import UniversalSpider
from Scrapy_crawl.utils import get_config
from scrapy.crawler import CrawlerProcess


def run():
    name = sys.argv[1]  # 输入参数
    custom_settings = get_config(name)  # 获取JSON配置文件信息
    spider = custom_settings.get('spider', 'universal')  # 爬取使用的爬虫名称
    project_settings = get_project_settings()  # 声明配置
    settings = dict(project_settings.copy())
    settings.update(custom_settings.get('settings'))  # 获取到的settings配置和项目全局的settings配置做了合并
    process = CrawlerProcess(settings)  # 新建一个CrawlerProcess，传入爬取使用的配置
    process.crawl(spider, **{'name': name})  # 启动爬虫
    process.start()


if __name__ == '__main__':
    run()
