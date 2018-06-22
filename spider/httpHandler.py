from urllib import request
# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
# http_handler = request.HTTPHandler(debuglevel=1)
# 构建 代理对象

cRequest = request.Request('http://api.xicidaili.com/free2016.txt')
r = request.urlopen(cRequest)
data = r.read()
print(data)
http_handler = request.ProxyHandler()
# 创建opener
opener = request.build_opener(http_handler)
# 构建请求
request = request.Request('http://www.baidu.com')
# 请求
try:
    response = opener.open(request)
except Exception as e:
    print(str(e))
    exit(1)

print('\n')
print(response.read())

