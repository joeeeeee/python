import sys,time
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scrapy import cmdline

cmdline.execute("scrapy crawl tencent".split())





