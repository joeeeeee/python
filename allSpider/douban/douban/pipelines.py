# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
import pymongo
from scrapy.conf import settings
from scrapy.pipelines.images import ImagesPipeline

class DoubanPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        account = settings['MONGODB_ACCOUNT']
        password = settings['MONGODB_PASSWORD']
        client = pymongo.MongoClient(host, port)
        db = client.admin
        db.authenticate(account, password)
        mdb = client[dbname]
        self.post = mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        # 向指定的表里添加数据
        # self.post.remove()
        row = self.post.find_one({'title': item['title']})
        if row:
            update_filter = {'_id': row['_id']}
            self.post.update_one(filter=update_filter, update={'$set': data})
        else:
            self.post.insert_one(data)
        return item

class ImagesPipeline(ImagesPipeline):
#
    # get_media_requests的作用就是为每一个图片链接生成一个Request对象，这个方法的输出将作为item_completed的输入中的results，
    # results是一个元组，每个元组包括(success, imageinfoorfailure)。如果success=true，imageinfoor_failure是一个字典，包括url/path/checksum三个key。
    def get_media_requests(self, item, info):
        image_url = item["imageUrl"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，就放到 image_path里，ImagesPipeline源码剖析可见
        image_path = [x["path"] for ok, x in results if ok]
        # os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["title"] + ".jpg")
        item["imagePath"] = settings['IMAGES_STORE'] + '/' + image_path[0]
        return item
