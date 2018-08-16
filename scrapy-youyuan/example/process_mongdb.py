#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""A script to process items from a redis queue."""
import pymongo
import json
import redis
from scrapy.conf import settings

from scrapy_redis import get_redis


def main():
    host = settings['MONGODB_HOST']
    port = settings['MONGODB_PORT']
    dbname = settings['MONGODB_DBNAME']
    account = settings['MONGODB_ACCOUNT']
    password = settings['MONGODB_PASSWORD']
    # 指定Mongdb 数据库信息
    mongoCli = pymongo.MongoClient(host, port)
    db = mongoCli.admin
    db.authenticate(account, password)
    mdb = mongoCli[dbname]
    post = mdb['test']
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='118.25.22.86', port=6379, db=0)

    while True:
        key, data = rediscli.blpop(['hongniangSpider:items'])
        item = json.loads(data)
        post.insert(item)


if __name__ == '__main__':
        main()
