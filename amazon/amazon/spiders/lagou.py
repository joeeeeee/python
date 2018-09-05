# import scrapy
#
# class LagouSpider(scrapy.Spider):
#     """Spider that reads urls from redis queue (myspider:start_urls)."""
#     name = 'lagou'
#     # allowed_domains = ["www.lagou.com"]
#     url = ['https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false']
#     index = 1
#     keyword = 'PHP'
#
#     def start_request(self):
#         param = {
#             'first': True,
#             'pn': self.index,
#             'kd': self.keyword
#         }
#         print(param)
#         yield scrapy.FormRequest(
#             url=self.url,
#             formdata=param,
#             callback=self.parse
#         )
#
#     def parse(self, response):
#         print(response.text())
import random

import requests
import scrapy
import json
from scrapy.spiders import CrawlSpider
# from mySpider.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    # offset = 0
    index = 1
    keyword = 'PHP'

    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    start_urls = [
        url+'&1=1'
    ]

    def start_requests(self):
        useragents = [
            "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.46",
            "Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
        ]
        cookies = {
            "Cookie": "user_trace_token=20180521170108-882c2729-10fd-4b07-8d9a-34be775b5a11; _ga=GA1.2.582823569.1526893270; LGUID=20180521170110-817395e1-5cd5-11e8-823f-525400f775ce; JSESSIONID=ABAAABAAAIAACBI0C150C148E7F254733491E13C36D7971; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535701307,1535787658; TG-TRACK-CODE=search_code; LGRID=20180904094656-67afac80-afe4-11e8-8590-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536025616; SEARCH_ID=bbfac69464d149a18b173c6951b89b09"
        }
        params = {
            "first": "false",
            "pn": '3',
            "kd": 'PHP',
            "city": "深圳",
            "needAddtionalResult": 'false'
        }
        # 请求头部
        headers = {
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'User-Agent': random.choice(useragents),
            'Referer': 'https://www.lagou.com/jobs/list_PHP?px=default&city=%E6%B7%B1%E5%9C%B3'
        }

        # res = requests.post(url=req_url, headers=headers,
        #                     data=params, cookies=cookies)  # f发送请求
        # res_json = res.json()  # 获取json数据
        yield scrapy.FormRequest(
            url=self.url,
            headers=headers,
            formdata=params,
            callback=self.parse_content,
            cookies=cookies,
            dont_filter=True
        )

    def parse_content(self, response):
        res = json.loads(response.body_as_unicode())
        # for site in res:
        #     print(res[site])
        # exit()
        print(res)

        if res['code'] == '0':
            self.logger.warning("解析状态:" + str(response.status))
            self.logger.warning("解析链接：" + response.url)
        else:
            self.logger.warning("连接失败:")
        exit()
        data = res.content.positionResult.result
        print(data)


        # print(response)
        # data = json.loads(response.text)['data']

        # for i in data:
            # item = DouyuItem()
            # item['name'] = i['nickname']
            # item['imageUrls'] = i['vertical_src']
            # yield item

        # self.offset += 20

        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
