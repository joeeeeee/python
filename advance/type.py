import types

class Person(object):
    __slots__ = ('name', 'age')
    # def __init__(self):

    def move(self):
        print('==move==')
    def eat(self):
        print('eat')

@classmethod
def classMethod(cls):
    print('==classMethod==')
    cls.score = 10

@staticmethod
def staticMethod(cls):
    print('==staticMethod==')


p = Person()

p.move()

# p.score = 10
Person.test = classMethod
Person.test()
# print(Person.score)
print(p.score)