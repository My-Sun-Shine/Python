# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    """创建Item需要继承scrapy.Item类，定义类型scrapy.Field字段"""
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
