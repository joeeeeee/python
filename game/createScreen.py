import pygame
import time
import random

class Base(object):
    def __init__(self, name, screen):
        self.name = name
        self.screen = screen

class Plane(Base):
    def __init__(self, screen, name):
        super().__init__(screen, name)
        self.screen = screen
        self.image = pygame.image.load(self.imageUrl)
        self.bulletList = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        needDelItem = []
        for i in self.bulletList:
            if i.judge():
                needDelItem.append(i)

        for d in needDelItem:
            self.bulletList.remove(d)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def moveLeft(self):
        pass

    def moveRight(self):
        pass

    def moveDown(self):
        pass

    def moveUp(self):
        pass

    def fire(self):
        bullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(bullet)


class HeroPlane(Plane):
    def __init__(self, screen, name):
        self.x = 230
        self.y = 600
        self.imageUrl = './feiji/hero.gif'
        super().__init__(screen, name)

    def moveLeft(self):
        self.x = self.x - 10

    def moveRight(self):
        self.x += 10

    def moveDown(self):
        self.y += 10

    def moveUp(self):
        self.y -= 10


class EnemyPlane(Plane):
    def __init__(self, screen, name):
        self.x = 0
        self.y = 0
        self.imageUrl = './feiji/enemy0.png'
        self.direction = 'right'
        super().__init__(screen, name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.move()
        self.fire()

    def move(self):
        if self.direction == 'right':
            self.moveRight()
            if self.x > 480 - 50:
                self.direction = 'left'
        elif self.direction == 'left':
            self.moveLeft()
            if self.x < 0:
                self.direction = 'right'

    def moveLeft(self):
        self.x = self.x - 2

    def moveRight(self):
        self.x += 2

    def moveDown(self):
        self.y += 1

    def moveUp(self):
        self.y -= 1

    def fire(self):
        rand = random.randint(0, 99)
        if rand in [1, 2]:
            bullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletList.append(bullet)
        needDelItem = []
        for i in self.bulletList:
            if i.judge():
                needDelItem.append(i)

        for d in needDelItem:
            self.bulletList.remove(d)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()


class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 30
        self.y = y + 30
        self.screen = screen
        self.imageUrl = './feiji/bullet-1.gif'
        self.image = pygame.image.load(self.imageUrl)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 2

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class Bullet(object):

    def __init__(self, x, y, screen):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.imageUrl = './feiji/bullet-3.gif'
        self.image = pygame.image.load(self.imageUrl)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 2

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

def main():
    pygame.init()
    # 1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.窗口加载图片
    background = pygame.image.load('./feiji/background.png')

    # 3.加载飞机
    # hero = pygame.image.load('./feiji/hero.gif').convert()
    plant = HeroPlane(screen,'hero')
    enemyPlane = EnemyPlane(screen,'enemy')

    while True:
        # 将图片覆盖到窗口
        screen.blit(background, (0, 0))
        plant.display()
        enemyPlane.display()

        # 获取事件，如果是退出时间(防止卡死)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    plant.moveLeft()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    plant.moveRight()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    plant.moveDown()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    plant.moveUp()
                elif event.key == pygame.K_SPACE:
                    plant.fire()
        # 刷新页面
        print(plant.bulletList)
        pygame.display.update()

if __name__ == '__main__':
    main()