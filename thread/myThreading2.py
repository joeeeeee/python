import threading
import time

class myThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print('%s 执行 %s' % (self.name,i))


def test():
    for i in range(5):
        t = myThread()
        t.run()

if __name__ == '__main__':
    test()