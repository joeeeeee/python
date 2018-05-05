from functools import reduce


# map
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
print(list(r))

def e(x, y):
    return x * y
# reduce
l = reduce(e, [1, 2, 3, 4, 5])
print(l)


L = 'hello world'
print(L[::-1])
