# -*- coding: utf-8 -*-
import scrapy
import os
import sys

from scrapy import Selector
from sina.items import SinaItem


class SinacrwalSpider(scrapy.Spider):
    name = 'sinacrwal'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        selector = Selector(response)
        parent_selector = selector.xpath('//div[@class="article"]//div[contains(@id,"tab")]//div')
        items = []
        # 遍历父分类
        for i in parent_selector:
            try:
                title = i.xpath('.//h3/a/text()').extract()[0]
                url = i.xpath('.//h3/a/@href').extract()[0]
                path = "./path/"+title
                if not os.path.exists(path):
                    os.makedirs(path)
                # 子标题
                childTitle = i.xpath('.//ul[@class="list01"]/li/a/text()').extract()
                # 子链接
                childUrl = i.xpath('.//ul[@class="list01"]/li/a/@href').extract()

                # 遍历子分类
                for j in range(0, len(childTitle)):
                    item = SinaItem()
                    item['parentTitle'] = title
                    item['parentUrls'] = url
                    sub_path = path + '/' + childTitle[j]
                    if not os.path.exists(sub_path):
                        os.makedirs(sub_path)
                    item['subTitle'] = childTitle[j]
                    item['subUrls'] = childUrl[j]
                    item['subFilename'] = sub_path
                    items.append(item)

            except Exception as e:
                print(e)
        print(items)
        for item in items:
            yield scrapy.Request(url=item['subUrls'], meta={'meta_1': item}, callback=self.second_parse)

    def second_parse(self, response):
        selector = Selector(response)
        meta_1 = response.meta['meta_1']
        cur_page_urls = selector.xpath('//a/@href').extract()
        items = []
        for i in cur_page_urls:
            if i.startswith(meta_1['parentUrls']) and i.endswith('.shtml'):
                item = SinaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subUrls'] = meta_1['subUrls']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrls'] = i
                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['sonUrls'], meta={'meta_2': item}, callback=self.third_parse)

    def third_parse(self, response):
        selector = Selector(response)
        item = response.meta['meta_2']
        header = selector.xpath('//h1/text()').extract()
        if len(header) > 0:
            header = header[0]
        else:
            header = ''
        content_list = response.xpath('//div[@id=\"artibody\"]/p/text()').extract()
        content = ''
        for content_one in content_list:
            content += content_one.strip()

        item['head'] = header
        item['content'] = content
        yield item
