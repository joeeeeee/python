import json
strList = '[1,2,3,4]'
strDict = '{"city":"hangzhou","name":"wyz"}'

print(json.loads(strDict))

listStr = [{'city': '北京','name': 'wyz'}]
json.dump(listStr, open('listStr.json', 'w'), ensure_ascii=True)

j = json.load(open('listStr.json'))
print(j)