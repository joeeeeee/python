# 浅复制

a = [11, 22, 33]
b = a
a.append(44)

# [11, 22, 33, 44]
print(b)


# 深复制
a = [11, 22, 33]
b = a[:]
# b = copy.deepcopy(a)
a.append(44)

print(b)