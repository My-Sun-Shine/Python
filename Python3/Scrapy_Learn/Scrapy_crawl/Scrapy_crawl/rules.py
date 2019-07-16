#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time        ：2019/7/16 16:24
# @Author      ：Falling Stars
# @FileName    ：rules
# @Software    ：PyCharm
# @Description ：
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china': (
        Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    )
}