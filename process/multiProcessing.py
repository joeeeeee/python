import os

from multiprocessing import *
from time import sleep


def run_pro(name, age):
    for i in range(10):
        print('子进程正在运行中，name: %s，age:%s,pid:%s' % (name, age, os.getpid()))
        sleep(0.5)


if __name__ == '__main__':
    print('父进程： %s正在运行 ' % os.getpid())
    p = Process(target=run_pro, args=('test', '1'))
    p.start()
    sleep(1)
    p.terminate()
    p.join()
    print('进程结束')
