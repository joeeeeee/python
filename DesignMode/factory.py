# 工厂模式
class CarStore(object):
    def createCar(self):
        pass

    def order(self,carName):
        car = self.carFactory.createcar(carName)
        car.move()

class XianDaiCarStore(CarStore):
    def __init__(self):
        self.carFactory = CarFactory()

    def createCar(self):
        return self.carFactory.createcar('xiandai')

class XianDaiCar(object):
    def move(self):
        print('xiandai car moving')
    def shop(self):
        print(' car stop')

class FengTianCar(object):
    def move(self):
        print('fengtian car moving')

    def shop(self):
        print(' car stop')

class CarFactory(object):
    def createcar(self, carName):
        car = ''
        if carName == 'xiandai':
            car = XianDaiCar()
        elif carName == 'fengtian':
            car = FengTianCar()
        return car

