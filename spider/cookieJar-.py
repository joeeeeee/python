from urllib import request,parse
from http import cookiejar

# 构建一个存储和管理cookie 的对象
c = cookiejar.CookieJar()
# 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
handler = request.HTTPCookieProcessor(c)
# 根据handler创建对象opener
opener = request.build_opener(handler)
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
passport = {"email": "13713613028", "password": "wyz520576"}
# 转化为url 格式，并转bytes
data = parse.urlencode(passport).encode('utf-8')

# 构建请求
r = request.Request('http://www.renren.com/PLogin.do', data=data)
# opener发送请求
f = opener.open(r)
response = opener.open("http://www.renren.com/410043129/profile")

print(response.read().decode('utf-8'))

