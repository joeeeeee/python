
# Money
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

m = Money()
m.money = 10
print(m.money)




