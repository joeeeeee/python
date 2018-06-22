# 闭包
# 内部函数对外部函数的变量的引用 （闭包）
def test():
    number = 10
    def count():
        # number = 10
        nonlocal number
        number = number + 1
        print(number)
        return number
    return count

c = test()
c()
c()
# c.count()
# c.count()