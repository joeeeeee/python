from threading import Lock,Thread
import time

l1 = Lock()
l2 = Lock()
l2.acquire()
l3 = Lock()
l3.acquire()

class Thread1(Thread):
    def run(self):
        while True:
            if l1.acquire():
                print('===task 1 start====')
                time.sleep(1)
                l2.release()

class Thread2(Thread):
    def run(self):
        while True:
            if l2.acquire():
                print('===task 2 start====')
                time.sleep(1)
                l3.release()

class Thread3(Thread):
    def run(self):
        while True:
            if l3.acquire():
                print('===task 3 start====')
                time.sleep(1)
                l1.release()


t1 = Thread1()
t2 = Thread2()
t3 = Thread3()

t1.start()
t2.start()
t3.start()