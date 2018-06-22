from lxml import etree

html = etree.parse('./hellow.html')
# r = etree.tostring(html, pretty_print=True)
r = html.xpath('//li[last()]')
print(r)
for i in r:
    a = i.xpath('//a[@href="link1.html"]')
    print(a)
