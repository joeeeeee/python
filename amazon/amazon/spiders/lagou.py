"""
title:抓取拉勾网的数据
time:2018-01-22
author:No.96
"""
import requests
import time
import random
import csv

# 移动端头部信息
useragents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.46",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
]
cookies = {

}
# city城市
# positionName 职位关键字
# pageNo 页码
# pageSize 叶大小


def lagou(city, positionName, pageNo, pageSize):
    cookies = {
        "Cookie": "user_trace_token=20180521170108-882c2729-10fd-4b07-8d9a-34be775b5a11; _ga=GA1.2.582823569.1526893270; LGUID=20180521170110-817395e1-5cd5-11e8-823f-525400f775ce; JSESSIONID=ABAAABAAAIAACBI0C150C148E7F254733491E13C36D7971; _gid=GA1.2.1983724889.1535701305; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535701307; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; LGSID=20180831162528-6ac621b6-acf7-11e8-b30a-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535704627; LGRID=20180831163706-0b3189db-acf9-11e8-b30a-5254005c3644; SEARCH_ID=a7e1cc65e7f940bd9d6645da2297e386"
    }
    req_url = "https://m.lagou.com/search.json?"
    params = {
        "city": city,
        "positionName": positionName,
        "pageNo": pageNo,
        "pageSize": pageSize
    }
    # 请求头部
    headers = {
        'Host': 'm.lagou.com',
        'Origin': 'https://m.lagou.com/search.html',
        'User-Agent': random.choice(useragents)
    }

    res = requests.get(url=req_url, headers=headers,
                       params=params, cookies=cookies)  # f发送请求
    print(res.text)
    res_json = res.json()  # 获取json数据
    result = res_json['content']['data']['page']['result']
    return result  # 返回json数据


# 解析返回的json
def analyze(city, result,writer):
    filename = city + '.csv'
    for item in result:
        job = {
            "city": item['city'],
            "companyFullName": item['companyFullName'],
            "companyName": item['companyName'],
            "positionName": item['positionName'],
            "salary": item['salary']
        }
        writer.writerow(job)


if __name__ == "__main__":
    city = "上海"
    positionName = "数据挖掘"
    pageSize = 15
    filename = city+'.csv'
    with open(filename,'a') as f:
        fieldnames = ['city', 'companyFullName','companyName','positionName','salary']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(10):
            result = lagou(city, positionName, i, pageSize)
            time.sleep(2)
            analyze(city,result,writer)