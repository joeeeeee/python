# 列表生成器
import os

L = list(range(1, 10))
print(L)

L2 = [x * x for x in range(1, 10)]
print(L2)

L3 = [m + n for m in 'XYZ' for n in 'ABC']
print(L3)

# 当前文件夹下
L4 = [d for d in os.listdir('.')]
print(L4)

D = {'a': 'A', 'b': 'B', 'c': 'C'}
print(D.items())
for k, v in D.items():
    print(k, '=', v)
