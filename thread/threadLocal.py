import threading

thread_local = threading.local()

def test1():
    std = thread_local.student
    print('current_name :'+threading.current_thread().name + ';\n current_student'+std)

def test2(name):
    thread_local.student = name
    test1()



t1 = threading.Thread(target=test2,name='test2',args=('wu',))
t2 = threading.Thread(target=test2,name='test1',args=('zhou',))
t1.start()
t2.start()
# t1.join()
# t2.join()