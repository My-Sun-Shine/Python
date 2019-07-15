# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ImageItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    定义数据结果
    """
    # 定义MongoDB存储的Collection名称和MySQL定义的表名
    collection = table = 'images360'

    id = Field()
    url = Field()
    title = Field()
    thumb = Field()
