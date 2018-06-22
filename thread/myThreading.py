import threading
import time


def dancing():
    while True:
        print('dancing start')
        time.sleep(1)

def singing():
    while True:
        print('singing start')
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=dancing)
    t2 = threading.Thread(target=singing)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print('当前线程数%s' % len(threading.enumerate()))
        if length < 1:
            print('结束')
            break
