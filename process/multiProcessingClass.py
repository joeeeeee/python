import os

from multiprocessing import *
from time import sleep, time


class ProcessClass(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print('子进程(%s) 正在执行 父进程 正在执行(%s)' % (os.getpid(), os.getppid()))
        start_time = time()
        sleep(self.interval)
        end_time = time()
        print('执行时长:%s' % (end_time - start_time))

if __name__ == '__main__':
    p1 = ProcessClass(2)
    p1.start()
    sleep(1)
    p1.join()
    print('进程结束')
