from threading import Lock,Thread
import time
from queue import Queue
q = Queue()
class Producter(Thread):
    def run(self):
        global q
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    msg = '生产品' + str(i)
                    q.put(msg)
                    print(msg)
                    print('当前队列数量' + str(q.qsize()))
                time.sleep(0.5)


class Consumer(Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 100:
                for i in range(10):
                    msg = ' 消费 ' + str(q.get())
                    print(msg)
                    print('当前队列数量' + str(q.qsize()))
                time.sleep(0.2)

for n in range(500):
    q.put('初始品' + str(n))
for i in range(3):
    p = Producter()
    p.start()
for k in range(10):
    c = Consumer()
    c.start()
