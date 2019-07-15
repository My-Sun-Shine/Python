# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MongoPipeline(object):
    """将数据保存在MongoDB中"""
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.collection
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


class MysqlPipeline():
    """
    Mysql
    """
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        print(item['title'])
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item


class ImagePipeline(ImagesPipeline):
    """
    图片下载，Scrapy提供专门处理下载的Pipeline，包括文件下载和图片下载
    这里实现ImagesPipeline
    """
    def file_path(self, request, response=None, info=None):
        """
        返回文件名
        :param request: 当前下载对于的Request对象
        :param response:
        :param info:
        :return:
        """
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        """
        当单个Item完成下载的处理办法，因为并不是每一张图片的下载都会成功，所以需要分析下载结果并去除下载失败的
        如果某张图片下载失败，那么也不需要将其保存到数据库中
        :param results:下载结果，列表形式，列表的每一个元素就是一个元组
        :param item:
        :param info:
        :return:
        """
        # 遍历下载结果找出所有成功的下载列表，如果列表为空，那么该Item对应的图片下载失败，随时抛出异常
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        """
        :param item: 爬取生成的Item对象
        :param info:
        :return:
        """
        yield Request(item['url'])
