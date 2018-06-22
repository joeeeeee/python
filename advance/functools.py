# 偏函数
import functools

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

p = functools.partial(foo,1,2,3)
p()
p(a = 1)


# wraps函数
def note(func):
    @functools.wraps(func)
    def wrapper():
        print('note something')
        return func()
    return wrapper

@note
def test():
    "test function"
    print('I am test')

test()
print(test.__doc__)