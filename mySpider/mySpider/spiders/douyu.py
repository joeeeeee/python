import scrapy
import json
from scrapy.spiders import CrawlSpider
from mySpider.items import DouyuItem


class DouyuSpider(CrawlSpider):
    name = "douyu"
    allowed_domains = ["http://capi.douyucdn.cn"]
    offset = 0

    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        data = json.loads(response.text)['data']

        for i in data:
            item = DouyuItem()
            item['name'] = i['nickname']
            item['imageUrls'] = i['vertical_src']
            yield item

        self.offset += 20

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)




