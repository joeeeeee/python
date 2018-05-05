# 生成器
g = (x * x for x in range(1, 10))
# print(next(g))

# fib 数组
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)

while True:
    try:
        x = next(f)
        print('g', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


