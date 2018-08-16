from scrapy_redis.spiders import RedisSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from amazon.items import TencentItem
import os, sys, re

cwd = os.getcwd()
common_path = os.path.dirname(cwd) + '\..\common'
sys.path.append(common_path)
from common.redisdb import RedisServer
from scrapy_redis.spiders import RedisCrawlSpider
class DmozSpider(RedisCrawlSpider):
    """Follow categories and extract links."""
    name = 'tencent'
    # start_urls = [
    #     "http://hr.tencent.com/position.php?&start=0#a"
    # ]
    redis_key = "amazon:tencent:start_urls"
    # allowed_domains = ['hr.tencent.com']
    # start_urls = ['https://segmentfault.com/']

    page_lx = LinkExtractor(allow=('position.php\?&start=\d+#a'))
    self_lx = LinkExtractor(allow=('position_detail.php\?id=\d+'))

    rules = [
        Rule(page_lx, follow=True),
        Rule(self_lx, callback='parse_detail', follow=False),
    ]

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', 'tencent.com')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(DmozSpider, self).__init__(*args, **kwargs)

    def parse_detail(self, response):
        self.logger.warning("解析状态:" + str(response.status))
        self.logger.warning("解析链接：" + response.url)

        position = response.xpath('//td[@id="sharetitle"]/text()').extract_first()
        workplace = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract_first()
        work_type = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract_first()
        recruit_number = response.xpath('//tr[@class="c bottomline"]/td[3]/text()').extract_first()
        recruit_number = re.match("(\d)*",recruit_number).group()
        duty = response.xpath('//tr[@class="c"][1]//ul[@class="squareli"]/li')
        required = response.xpath('//tr[@class="c"][2]//ul[@class="squareli"]/li')
        word_duty = []
        work_required = []

        for i in duty:
            if len(i.xpath('./text()').extract()) > 0:
                word_duty.append(i.xpath('./text()').extract()[0])
        for r in required:
            if len(r.xpath('./text()').extract()) > 0:
                work_required.append(r.xpath('./text()').extract()[0])

        # exit()
        item = TencentItem()
        item['position'] = position
        item['workplace'] = workplace
        item['work_type'] = work_type
        item['recruit_number'] = recruit_number
        item['work_duty'] = ''.join(word_duty)
        item['work_required'] = ''.join(work_required)
        yield item

        # word_duty = response.

        # for i in response.xpath('//table[@class="tablelist"]//tr[@class="odd"] |' +
        #                         '//table[@class="tablelist"]//tr[@class="even"]'):
        #
        #     name = i.xpath('./td[1]/a/text()').extract()[0]
        #     detailLink = str("http://hr.tencent.com") + i.xpath('./td[1]/a/@href').extract()[0]
        #     if len(i.xpath('./td[2]/text()').extract()) > 1:
        #         workLocation = i.xpath('./td[2]/text()').extract()[0]
        #     else:
        #         workLocation = ''
        #
        #     peopleNumber = i.xpath('./td[3]/text()').extract()[0]
        #     workLocation = i.xpath('./td[4]/text()').extract()[0]
        #     publishTime = i.xpath('./td[5]/text()').extract()[0]
        #     # item = AmazonItem()
        #     # item['name'] = name
        #     # item['description'] = peopleNumber
        #     # item['detail_link'] = detailLink
        #     # item['work_location'] = workLocation
        #     # item['publishTime'] = publishTime
        #     yield item

    # def parse_directory(self, response):
    #     self.logger.warning("解析状态:" + str(response.status))
    #     self.logger.warning("解析链接：" + response.url)
    #     for i in response.xpath('//table[@class="tablelist"]//tr[@class="odd"] |' +
    #                             '//table[@class="tablelist"]//tr[@class="even"]'):
    #
    #         name = i.xpath('./td[1]/a/text()').extract()[0]
    #         detailLink = str("http://hr.tencent.com") + i.xpath('./td[1]/a/@href').extract()[0]
    #         if len(i.xpath('./td[2]/text()').extract()) > 1:
    #             workLocation = i.xpath('./td[2]/text()').extract()[0]
    #         else:
    #             workLocation = ''
    #
    #         peopleNumber = i.xpath('./td[3]/text()').extract()[0]
    #         workLocation = i.xpath('./td[4]/text()').extract()[0]
    #         publishTime = i.xpath('./td[5]/text()').extract()[0]
    #         # item = AmazonItem()
    #         # item['name'] = name
    #         # item['description'] = peopleNumber
    #         # item['detail_link'] = detailLink
    #         # item['work_location'] = workLocation
    #         # item['publishTime'] = publishTime
    #         yield item
