#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/16 16:21
# @Author      ：Falling Stars
# @FileName    ：loaders
# @Software    ：PyCharm
# @Description ：
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):  # 继承ItemLoader
    """TakeFirst返回列表的第一个非空值，类似extract_first()的功能"""
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):  # 继承NewsLoader
    """每个输入值经过Join()，再经过strip()"""
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())
