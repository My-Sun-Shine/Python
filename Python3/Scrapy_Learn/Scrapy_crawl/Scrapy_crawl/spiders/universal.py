# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Scrapy_crawl.items import *
from Scrapy_crawl.loaders import *
from Scrapy_crawl.utils import get_config
from Scrapy_crawl import urls
from Scrapy_crawl.rules import rules


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)  # 获取配置文件
        self.config = config
        self.rules = rules.get(config.get('rules'))  # 获取Rule名称，然后去rules类中获取对应的Rule配置
        start_urls = config.get('start_urls')  # 获取start_urls配置
        if start_urls:
            if start_urls.get('type') == 'static':  # 静态类型，直接获取连接
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':  # 动态类型
                self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args', [])))
        self.allowed_domains = config.get('allowed_domains')  # 获取主机
        super(UniversalSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get('item')  # 获取解析函数配置信息
        if item:
            cls = eval(item.get('class'))()#获取Item类
            loader = eval(item.get('loader'))(cls, response=response)#获取loader
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            yield loader.load_item()
