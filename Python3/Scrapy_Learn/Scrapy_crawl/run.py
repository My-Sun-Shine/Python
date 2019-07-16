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
    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()