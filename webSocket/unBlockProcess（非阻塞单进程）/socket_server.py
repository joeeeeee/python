import socket

g_socket_list = []

def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 9887))
    s.listen(1000)
    s.setblocking(False)

    while True:
        try:
            ac = s.accept()
        except Exception as e:
            pass
        else:
            print('新的客户端来到：%s' % str(ac))
            ac[0].setblocking(False)
            g_socket_list.append(ac)

        delete_socket_list = []
        for conn, address in g_socket_list:
            try:
                content = s.recv(1024)
                if content == '':
                    # conn.close()
                    delete_socket_list.append((conn,address))
                else:
                    print(str(content,encoding='utf8'))

            except Exception as e:
                pass

        for d in delete_socket_list:
            g_socket_list.remove(d)

if __name__ == '__main__':
    main()





