# -*- coding: utf-8 -*-
import re
import scrapy
from douban.items import DoubanItem

class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    start = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url + str(start)]

    def parse(self, response):
        selector = scrapy.Selector(response)
        articles = selector.xpath('//div[@class="article"]//ol/li')
        items = []
        for i in articles:
            item = DoubanItem()
            image_url = i.xpath('./div[@class="item"]//div[@class="pic"]/a/img/@src').extract()
            if len(image_url) > 0:
                item['imageUrl'] = image_url[0]
            else:
                item['imageUrl'] = ''
            title = i.xpath('./div[@class="item"]/div[@class="info"]//span[@class="title"]/text()').extract()
            if len(title) > 0:
                title = list(map(lambda x: x.replace('\xa0', ''), title))
                item['title'] = "".join(title)
            score = i.xpath('./div[@class="item"]//span[@class="rating_num"]/text()').extract()
            if len(score) > 0:
                item['score'] = float(score[0])
            content = i.xpath('./div[@class="item"]//div[@class="bd"]/p[1]/text()').extract()
            if len(content) > 0:
                content = content[0]
                p = re.compile(r'[\xa0 | \' |\n]')
                content = p.sub('', content)
                item['content'] = content
            info = i.xpath('./div[@class="item"]//p[@class="quote"]/span/text()').extract()
            if len(info) > 0:
                item['info'] = info[0]
            yield item
            item['rank'] = int(i.xpath('./div[@class="item"]/div[@class="pic"]/em/text()').extract()[0])

        if self.start <= 225:
            self.start += 25
            yield scrapy.Request(self.url + str(self.start), callback=self.parse)
        pass
