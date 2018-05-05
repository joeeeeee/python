# 迭代器
from collections import Iterable
d = {'1': 1, '2': 2}
if isinstance('abc', Iterable):
    for k in d:
        print(d[k])
        print(k)

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration as e:
        print(e.value)
        break


