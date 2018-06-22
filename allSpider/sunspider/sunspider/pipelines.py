# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class SunspiderPipeline(object):
    def __init__(self):
        self.f = open('data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        s = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # s = str(s,='GBK')
        self.f.write(s)
        return item

    def close_spider(self, spider):
        self.f.close()
