import threading
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("---test1---g_num=%d" % g_num)



def test2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("---test2---g_num=%d" % g_num)


t = threading.Thread(target=test1)
t.start()
time.sleep(0.01)

t2 = threading.Thread(target=test2)
t2.start()

print("---g_num=%d---"%g_num)