import socket

# 创建socket 对接
c = socket.socket()
# 连接地址和端口号
c.connect(('127.0.0.1', 8088))
while True:
    # 输入数据
    sendData = input('请输入需要传输的数据\n')
    # 传输数据
    c.sendall(bytes(sendData, encoding='utf8'))
    if sendData == 'bye':
        break
    # 接受服务器传输过来的数据
    accept_data = c.recv(1024)
    print(str(accept_data,encoding='utf8'))
# 关闭连接
c.close()
