import scrapy
import json
from scrapy.spiders import CrawlSpider
from douyuspider.items import DouyuspiderItem


class DouyuSpider(CrawlSpider):
    name = "douyu"
    allowed_domains = ["www.acfun.cn/index/change"]
    offset = 2

    url = 'http://www.acfun.cn/index/change?channelId=60&page='
    # url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        data = {}
        try:
            data = json.loads(response.text)['data']['hits']
        except Exception as e:
            print(e)
        # yield
        for i in data:
            item = DouyuspiderItem()
            item['name'] = i['title']
            item['imageUrls'] = i['image']
            yield item

        self.offset += 1

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)







