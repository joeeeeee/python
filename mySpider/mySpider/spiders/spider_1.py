import scrapy

from mySpider.items import ItcastItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ItcastSpider(CrawlSpider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/channel/teacher.shtml',
    )

    page_lx = LinkExtractor(allow=("start=(\d+)"))

    rule = [
        Rule(page_lx, callback='parse_content', follow=True)
    ]

    def parse_content(self, response):
        items = []
        print(response.text)
        exit()
        # for each in response.xpath("//div[@class='li_txt']"):
        # print(response.xpath("//div[@class='li_txt']"))
        # exit()
        for i in response.xpath("//div[@class='li_txt']"):
            item = ItcastItem()

            name = i.xpath('h3/text()').extract()
            title = i.xpath('h4/text()').extract()
            info = i.xpath('p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            yield item


        # return items


