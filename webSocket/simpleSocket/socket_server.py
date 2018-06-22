import socket

# 创建 socket
s = socket.socket()
# 绑定ip 和端口号
s.bind(('127.0.0.1', 8088))
# 监听端口 最大连接数 5
s.listen(5)
while True:
    # accept 阻塞
    conn, attr = s.accept()
    print('===新建连接===')
    while True:
        # 接受 请求的数据 1024 个字节。以字符串方式返回
        recv_data = conn.recv(1024)
        # 将编码转成utf8
        recv_data2 = str(recv_data, encoding="utf8")
        print('接受数据'+recv_data2)
        if recv_data2 == 'bye':
            print('当前连接请求关闭')
            break
        print(recv_data2)
        # 发送的内容
        send_data = input('输入发送的内容\n')
        # 发送数据
        conn.sendall(bytes(send_data, encoding='utf8'))
    # 连接关闭
    conn.close()
    print('===连接关闭===')
