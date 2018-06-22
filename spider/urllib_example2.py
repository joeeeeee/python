from urllib import request,parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


print('Login to weibo.cn...')
phone = '13713613028'
passwd = 'wyz520576'
logdata = parse.urlencode([
    ('username', phone),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', 1),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'),
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=logdata.encode('utf-8')) as f:
    for k, v in f.getheaders():
        print(k + ':' + v)
    print('data:' + f.read().decode('utf-8'))