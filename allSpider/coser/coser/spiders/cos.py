# -*- coding: utf-8 -*-
import scrapy


class CosSpider(scrapy.Spider):
    name = 'cos'
    allowed_domains = ['bcy.net']
    start_urls = ['http://bcy.net/']

    def parse(self, response):
        pass
