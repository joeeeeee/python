import os

from multiprocessing import *
from time import sleep, time


def run_pro(interval):
    start_time = time()
    sleep(interval)
    print('子进程正在运行中 子进程 %s ，主进程pid %s' % (os.getpid(), os.getppid()))
    end_time = time()
    print('子进程执行时间 %0.2f' % (end_time - start_time))

def run_pro2(interval):
    start_time = time()
    sleep(interval)
    print('子进程正在运行中 子进程 %s ，主进程pid %s' % (os.getpid(), os.getppid()))
    end_time = time()
    print('子进程执行时间 %0.2f' % (end_time - start_time))


if __name__ == '__main__':
    p1 = Process(target=run_pro, args=(1,))
    p2 = Process(target=run_pro2, args=(2,))
    p1.start()
    p2.start()
    sleep(1)
    print('%s p2 子进程状态 is_active:%s' % (p2.name, p2.is_alive()))
    p1.join()
    p2.join()
    print('%s p2 子进程状态 is_active:%s' % (p2.name, p2.is_alive()))
    print('进程结束')