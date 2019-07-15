# -*- coding: utf-8 -*-
import scrapy
from Scrapy_A.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # 项目的唯一名字，区分不同的Spider
    allowed_domains = ['quotes.toscrape.com']  # 允许爬取的域名，如果初始或后续的请求链接不是这个域名下的，则请求链接会被过滤掉
    start_urls = ['http://quotes.toscrape.com/']  # 爬虫启动时爬取的url列表，初始请求由它来定义

    def parse(self, response):  # 该方法负责解析返回的响应、提取数据或者进一步生成要处理的请求
        """
        response是start_urls里面的链接爬取后的结果，使用parse方法进行解析
        使用CSS选择器或者XPath选择器
        """
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()  # 声明数据类Item
            # extract_first()方法获取第一个元素
            # extract()方法获取所有结果组成的列表
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        # 获取下一页
        next_page = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next_page)
        # url：请求链接；callback：回调函数，当得到url响应的时候，回调parse()方法
        yield scrapy.Request(url=url, callback=self.parse)
