# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os
import json

class DouyuspiderPipeline(ImagesPipeline):
    test = 'E:\images'
    IMAGE_STORE = 'E:\images'
#
    # get_media_requests的作用就是为每一个图片链接生成一个Request对象，这个方法的输出将作为item_completed的输入中的results，
    # results是一个元组，每个元组包括(success, imageinfoorfailure)。如果success=true，imageinfoor_failure是一个字典，包括url/path/checksum三个key。
    def get_media_requests(self,item, info):
        image_url = item["imageUrls"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 固定写法，获取图片路径，同时判断这个路径是否正确，如果正确，就放到 image_path里，ImagesPipeline源码剖析可见
        image_path = [x["path"] for ok, x in results if ok]
        # os.rename(self.test + "/" + image_path[0], self.test + "/" + item["name"] + ".jpg")
        item["imagesPath"] = self.test + "/" + item["name"]

