from urllib import request
# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
# http_handler = request.HTTPHandler(debuglevel=1)
# 构建 代理对象

header = {
    'Host': 'local.sa.hqygou.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'Cookie':'language=iTawIxLi8sU%3D; PHPSESSID=4qkmgnm5nibm3lra1ervn1lb17',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
cRequest = request.Request('http://local.sa.hqygou.com', headers=header)
r = request.urlopen(cRequest)
data = r.read()
print('\n')
print(data)

