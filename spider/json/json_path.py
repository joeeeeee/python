from urllib import request
import json
import jsonpath

req = request.Request('http://www.lagou.com/lbs/getAllCitySearchLabels.json')
res = request.urlopen(req)
data = json.loads(res.read())
d = jsonpath.jsonpath(data, '$..data..name')
print(d)
print(d.decode())
