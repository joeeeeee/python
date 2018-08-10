from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?&start=0#a"
    ]
    # allowed_domains = ['segmentfault.com']
    # start_urls = ['https://segmentfault.com/']

    rules = [
        Rule(LinkExtractor(allow=("start=\d+"),unique=False), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):

        for i in response.xpath('//table[@class="tablelist"]//tr[@class="odd"] |' +
                                '//table[@class="tablelist"]//tr[@class="even"]'):

            name = i.xpath('./td[1]/a/text()').extract()[0]
            detailLink = str("http://hr.tencent.com") + i.xpath('./td[1]/a/@href').extract()[0]
            if len(i.xpath('./td[2]/text()').extract()) > 1:
                workLocation = i.xpath('./td[2]/text()').extract()[0]
            else:
                workLocation = ''
            peopleNumber = i.xpath('./td[3]/text()').extract()[0]
            workLocation = i.xpath('./td[4]/text()').extract()[0]
            publishTime = i.xpath('./td[5]/text()').extract()[0]


            # 获取下一个链接
            # curPage = re.search('(\d+)', response.url).group(1)
            # curPage = int(curPage) + 10
            #
            # url = re.sub('\d+', str(curPage), response.url)

            # yield scrapy.Request(url, callback=self.parse)

        # for div in response.css('.title-and-desc'):
            yield {
                'name': name,
                'description': peopleNumber,
                'link': detailLink,
            }
