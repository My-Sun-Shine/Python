# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        """
        该方法必须返回包含数据的字典或Item对象或者抛出异常
        item：每次爬虫生成的Item对象
        spider：爬虫实例
        """
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].strip() + '...'
            return item
        else:
            return DropItem("Missing Text")


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri  # 链接
        self.mongo_db = mongo_db  # 数据库名

    @classmethod  # 标识这是一个依赖注入的方式
    def from_crawler(cls, crawler):
        """
        :param crawler: 得到全局配置的每个配置信息来自settings.py
        :return:
        """
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        """
        当爬虫开启的时候，这个方法被调用
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        """实现数据插入"""
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        """
        爬虫关闭的时候，该方法被调用
        """
        self.client.close()
