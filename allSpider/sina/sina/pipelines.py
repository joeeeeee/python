# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def process_item(self, item, spider):
        print('==============')
        print(1111)
        print('==============')
        sonUrls = item['sonUrls']
        filename = sonUrls[7:-6].replace('/', '_')
        filename += ".txt"
        print(item['subFilename'] + '/' + filename)
        fp = open(item['subFilename'] + '/' + filename, 'w',encoding='utf-8')
        fp.write(item['content'])
        fp.close()

        return item
