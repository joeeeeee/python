# 装饰器
# 1. 引⼊⽇志
# 2. 函数执⾏时间统计
# 3. 执⾏函数前预备处理
# 4. 执⾏函数后清理功能
# 5. 权限校验等场景
# 6. 缓存

# 不带参数
from time import ctime,sleep

def timefun(func):
    def wrapperfunc():
        print('%s call at time %s' % (func.__name__, ctime()))
        func()
    return wrapperfunc


@timefun
def foo():
    print('decoration')

foo()

# 带参数
def timefunc(func):
    def wrapperfunc(a, b):
        print('%s call at time %s' % (func.__name__, ctime()))
        func(a, b)
    return wrapperfunc

@timefunc
def foo(a, b):
    print('%s == %s' % (a, b))

foo(1, 2)

# 多参数
def timefunc(func):
    def wrapperfunc(*args, **kwargs):
        print('%s call at time %s' % (func.__name__, ctime()))
        func(*args, **kwargs)
    return wrapperfunc

@timefunc
def foo(a, b, c):
    print('%s == %s' % (a, b))
    print(c)

foo(1, 2, {'key' : 'word'})

# return func

def timefunc(func):
    def wrapperfunc(*args, **kwargs):
        print('%s call at time %s' % (func.__name__, ctime()))
        # func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapperfunc

@timefunc
def foo(a, b, c):
    print('%s == %s' % (a, b))
    print(c)
    return 'hahaha'

foo(1, 2, {'key' : 'word'})
print(foo(1, 2, {'key' : 'word'}))


# 添加外部参数
# 添加外部参数时 多添加一层结构，专门传参用
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

foo()

# 类装饰器
# 装饰器函数其实是这样⼀个接⼝约束， 它必须接受⼀个callable对象作为参
# 数， 然后返回⼀个callable对象。 在Python中⼀般callable对象都是函数， 但
# 也有例外。 只要某个对象重写了 __call__() ⽅法， 那么这个对象就是
# callable的
class Test(object):
    def __init__(self, func):
        print('初始化参数开始========')
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('调用开始')
        self.__func()

@Test
def foo():
    print('开始测试')

foo()