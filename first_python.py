#
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1('a','b','c','d','e',**{'test':'test'})
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
# f1('test', 'test2', 10, 10,20,30, **{'args': 'args'});

#
# def counts(*num):
#     sum = 0
#     for i in num:
#         sum += i
#     print(sum)
#
#
# counts(1, 2)

#L = tuple(range(100))
#print(L[-10::2])

# from collections import Iterable
# print(isinstance('abc', Iterable))
# import os
# dir = []
# dir = [d for d in os.listdir('.')]
# print(dir)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
# 
#     return 'done'
# 
# for i in fib(10):
#     print(i)
# 
# g = fib(10)
# while True:
#     try:
#         n = next(g)
#         print('g:', n)
#     except StopIteration as e:
#         print('return value:', e.value)
#         break
#
# def triangles(max):
#     n=0
#     list=[]
#     while n<max:
#         if n==0:
#                 list=[1]
#         elif n==1:
#                 list=[1,1]
#         else:
#             print(range(len(list)-1))
#             list=[list[i]+list[i+1] for i in range(len(list)-1)]
#             print(list)
#             list.insert(0,1)
#             list.append(1)
#         n=n+1
#         yield list
#
# g=triangles(10)
#
# # t = range(0, 3)
# for i in g:
#     print(i)
# while True:
#     # next(g)
# from functools import reduce
#
# l = list(range(10))
#
# def f(x):
#     return x * x;
#
# r = list(map(f,l))
# # print(r);
# def r(x,y):
#     return x+y
# print(reduce(r,l))

# def createCounter():
#     n = [0]
#     def counter():
#         # nonlocal n
#         n[0] = n[0] + 1
#         print(n[0])
#     return counter
#
# counter = createCounter()
# counter()
# counter()
# counter()
# createCounter()
# createCounter()

# ls = list(filter(lambda n: n % 2 == 0, range(0, 20)))
# print(ls)

# def log(func):
#     def wrapper(*args,**kw):
#         print('call func %s'% func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('10101010')

# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s call func %s'% (text,func.__name__))
#             # print(wrapper.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('10101010')
#     print(now.__name__)
#
# now()

# import functools
# int2 = functools.partial(int, base=2)
# print(int2('1000000'))