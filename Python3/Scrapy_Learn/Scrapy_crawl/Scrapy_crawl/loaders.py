#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/16 16:21
# @Author      ：Falling Stars
# @FileName    ：loaders
# @Software    ：PyCharm
# @Description ：
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())