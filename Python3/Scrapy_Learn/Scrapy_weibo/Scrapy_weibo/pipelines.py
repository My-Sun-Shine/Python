# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import re
import time
import pymongo

from Scrapy_weibo.items import *


class TimePipeline():
    """
    添加一个爬取时间
    """
    def process_item(self, item, spider):
        if isinstance(item, UserItem) or isinstance(item, WeiboItem):
            now = time.strftime('%Y-%m-%d %H:%M', time.localtime())
            item['crawled_at'] = now
        return item


class WeiboPipeline():
    def parse_time(self, date):
        """
        统一转换时间
        :param date:
        :return:
        """
        if re.match('刚刚', date):
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        if re.match('\d+分钟前', date):
            minute = re.match('(\d+)', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(minute) * 60))
        if re.match('\d+小时前', date):
            hour = re.match('(\d+)', date).group(1)
            date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - float(hour) * 60 * 60))
        if re.match('昨天.*', date):
            date = re.match('昨天(.*)', date).group(1).strip()
            date = time.strftime('%Y-%m-%d', time.localtime() - 24 * 60 * 60) + ' ' + date
        if re.match('\d{2}-\d{2}', date):
            date = time.strftime('%Y-', time.localtime()) + date + ' 00:00'
        return date

    def process_item(self, item, spider):
        if isinstance(item, WeiboItem):
            if item.get('created_at'):
                item['created_at'] = item['created_at'].strip()
                item['created_at'] = self.parse_time(item.get('created_at'))
            if item.get('pictures'):
                item['pictures'] = [pic.get('url') for pic in item.get('pictures')]
        return item


class MongoPipeline(object):
    """
    保存到数据库
    """
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        # 添加了Collection的索引，在这里为两个Item都添加了索引，索引的字段是id
        # 由于这次是大规模爬取，爬取过程涉及数据的更新问题，所以为每个Collection建立了索引，这样可以大大提高检索效
        self.db[UserItem.collection].create_index([('id', pymongo.ASCENDING)])
        self.db[WeiboItem.collection].create_index([('id', pymongo.ASCENDING)])

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, UserItem) or isinstance(item, WeiboItem):
            # update方法第一个参数是查询条件，第二个参数是爬取的Item
            # 使用了$set操作符，如果爬取到重复的数据即可对数据进行更新，同时不会删除已存在的字段
            # 不加$set操作符，那么会直接进行item替换，这样可能会导致已存在的字段如关注和粉丝列表清空
            # 第三个参数设置为True，如果数据不存在，则插入数据。这样就可以做到数据存在即更新、数据不存在即插入，从而获得去重的效果
            self.db[item.collection].update({'id': item.get('id')}, {'$set': item}, True)
        if isinstance(item, UserRelationItem):
            # $addToSet操作符可以向列表类型的字段插入数据同时去重,它的值就是需要操作的字段名称
            # $each操作符对需要插入的列表数据进行了遍历,以逐条插入用户的关注或粉丝数据到指定的字段
            self.db[item.collection].update(
                {'id': item.get('id')},
                {'$addToSet':
                    {
                        'follows': {'$each': item['follows']},
                        'fans': {'$each': item['fans']}
                    }
                }, True)
        return item
