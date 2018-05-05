# 切片
# 索引 n开始 到索引 ( n -1)
L = ['sara', 'joe']
print(L[0:1])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
t = (0, 1, 2, 3, 4, 5)[:3]
print(t)
