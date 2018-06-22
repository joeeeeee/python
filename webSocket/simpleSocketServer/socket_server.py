import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            conn = self.request
            address = self.client_address
            while True:
                acceptData = str(conn.recv(1024), encoding='utf8')
                if acceptData == 'bye':
                    break
                sendData = bytes(input('请输入发送的数据\n'), encoding='utf8')
                conn.sendall(sendData)
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8087), MyServer)
    server.serve_forever()