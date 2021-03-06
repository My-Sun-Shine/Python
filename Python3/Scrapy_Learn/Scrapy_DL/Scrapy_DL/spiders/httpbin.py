# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    def parse(self, response):
        self.logger.debug('HTML Text：' + response.text)
        self.logger.debug('Status Code：' + str(response.status))
