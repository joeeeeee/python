import re

pattern = re.compile(r'\d+\.\d*')
v = '1234,50,50123,123.123,1231,151.151'

m = pattern.finditer(v)
print(type(m))

for i in m:
    print()
    print('matching string: {}, position: {}'. format(i.group(), i.span()))


pattern = re.compile(r'[\s\,\;]')

v = 'a,b,c;c d e'
m = pattern.split(v)
print(m)

string = 'hello world test tewst2'

p = re.compile(r'(\w+) (\w+)')
t1 = p.sub(r'hello worlds', string)
t2 = p.sub(r'\2 \1', string)
print(t2)


title = '测试 测试'
p = re.compile(r'[\u4e00-\u9fa5]+')
data = p.findall(title)
print(data)




