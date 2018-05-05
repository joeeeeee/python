L = 'hello world'
print(L[::-1])

# find
index = L.find('world')
print(index)

# split
print(L.split(' '))

# join
print(L)
t = L.split(' ')
print(t)
print('-'.join(t))

A = ['hello world', 'test']

# fileName = input('请输入')
# if fileName in A:
#     print('已存在')
# else:
#     print('不存在')

a = [1, 2, 3, 4]
a.reverse()
print(a)
a.sort()
print(a)

for i, char in enumerate(a):
    print(i, ' = ', char)

test = [1,]

def test1():
    # global a
    test.extend([3, 4, 5])

test1()
print(test)

# 可变类型与不可变类型
#   可变类型， 值可以改变：
#       列表 list
#       字典 dict
#   不可变类型， 值不可以改变：
#       数值类型 int, long, bool, float
#       字符串 str
#       元组 tuple


sum = lambda x, y: x * y
print(sum(10, 2))

stus = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]
stus.sort(key = lambda x: x['age'] ,reverse= True)
print(stus)


