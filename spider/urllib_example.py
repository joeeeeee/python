from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
req = request.Request('https://api.douban.com/v2/book/2129650')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
f = request.urlopen(req)
for k, v in f.getheaders():
    print(k + ':' + v)
print('data:' + f.read().decode('utf-8'))