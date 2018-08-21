import redis
from functools import wraps
import os,configparser

def singleton(cls):
    instance = {}

    @wraps(cls)
    def getInstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getInstance


# @singleton
class RedisServer(object):
    def __init__(self):
        path = os.path.dirname(__file__)
        config_url = path + '/config.ini'
        config = configparser.ConfigParser()
        config.read(config_url)
        host = config.get('redis', 'host')
        port = config.get('redis', 'port')
        auth = config.get('redis', 'auth')
        redis_pool = redis.ConnectionPool(host=host, port=port, password=auth)
        self.redis_server = redis.Redis(connection_pool=redis_pool)

