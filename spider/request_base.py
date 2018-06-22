import requests

kw = {'kw': '长城'}

req = requests.request('get', 'http://www.baidu.com', params = kw)

print(req.content.decode())

print(req.status_code)

print(req.cookies)

cookiedict = requests.utils.dict_from_cookiejar(req.cookies)
print(cookiedict)
