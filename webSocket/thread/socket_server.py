from socket import *
from threading import Thread

def dealProcess(conn, address):
    while True:
        recvData = str(conn.recv(1024), encoding='utf8')
        if recvData == '':
           print('%s 已断开' % address)
           break
        else:
           print('%s 发送数据:%s' % (address, recvData))
    conn.close()


def main():
    serSocket = socket()
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serSocket.bind(('127.0.0.1', 8091))
    serSocket.listen(5)
    try:
        while True:
            conn, address = serSocket.accept()
            client = Thread(target=dealProcess, args=(conn, address))
            client.start()
            # 因为线程中共享这个套接字，如果关闭了会导致这个套接字不可用，
            # 但是此时在线程中这个套接字可能还在收数据，因此不能关闭
            # conn.close()
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()

