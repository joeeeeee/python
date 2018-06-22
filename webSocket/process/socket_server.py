from socket import *
from multiprocessing import *

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
    serSocket.bind(('127.0.0.1', 8090))
    serSocket.listen(5)
    try:
        while True:
            conn, address = serSocket.accept()
            client = Process(target=dealProcess, args=(conn, address))
            client.start()
            conn.close()
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()

