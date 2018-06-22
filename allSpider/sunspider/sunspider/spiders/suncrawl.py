# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from sunspider.items import SunspiderItem


class SuncrawlSpider(CrawlSpider):
    name = 'suncrawl'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    page_link = LinkExtractor(allow=('type=4'))
    content_link = LinkExtractor(allow=r'/html/question/\d+/\d+.shtml')

    rules = [
        Rule(page_link, process_links='deal_links', follow=True),
        Rule(content_link, callback='parse_content')
    ]
    # def parse(self, response):
    #     pass

    def deal_links(self, links):
        for link in links:
            print(link.url)
            link.url = link.url.replace("?", "&").replace("Type&", "Type?")
            # print(link.url)
        return links

    def parse_content(self, response):
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