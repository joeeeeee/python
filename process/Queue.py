from multiprocessing import Process, Pool, Manager
import os
import time


def write(q):
    for i in range(1,1000):
        time.sleep(0.01)
        q.put(i)
        print('push %s to queue' % i)


def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('read %s from queue' % value)
            time.sleep(0.2)


if __name__ == '__main__':
    q = Manager().Queue()
    poll = Pool()
    poll.apply_async(write, (q,))
    poll.apply_async(read, (q,))
    poll.close()
    poll.join()
