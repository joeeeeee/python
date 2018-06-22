# -*- coding: utf-8 -*-
import re
import scrapy
from sunspider.items import SunspiderItem

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        l = response.xpath('//div[@class="greyframe"]//a[@class="news14"]/@href').extract()

        for i in l:
            yield scrapy.Request(i, callback=self.parse_detail)

        if self.offset <= 71130:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_detail(self, response):
        item = SunspiderItem()
        header = response.xpath('//div[@class="ctitle"]//strong[@class="tgray14"]/text()').extract()

        if len(header) >= 1:
            text = header[0]
            text = text.strip().split('\xa0')
            number = text[-1].split(':')[-1]
            title = text[0].split('：')[-1]
        else:
            pass

        content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()

        if len(content) >= 1:
            content = map(lambda c: c.strip(), content)
            content = "".join(content).strip()
            p = re.compile(r'[\xa0 | \']')
            content = p.sub('', content)

        else:
            content = ''
        item['title'] = title
        item['number'] = number
        item['content'] = content
        item['url'] = response.url

        yield item

