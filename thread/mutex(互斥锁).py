from threading import Thread ,Lock
import time

g_num = 0
mutex = Lock()

def test1():
    global g_num
    for i in range(1000000):
        # 获取锁
        mutexFlag = mutex.acquire(True)
        if mutexFlag :
            g_num += 1
            mutex.release()
    print("---test1---g_num=%d" % g_num)

def test2():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
            mutex.release()
    print("---test2---g_num=%d" % g_num)


t = Thread(target=test1)
t.start()
time.sleep(0.01)

t2 = Thread(target=test2)
t2.start()

print("---g_num=%d---"%g_num)