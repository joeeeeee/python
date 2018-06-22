from socket import *

# 建立UPD链接
s = socket(AF_INET, SOCK_DGRAM)
# IP地址和端口号
senderAddress = ('10.18.5.4', 8080)
# 输入关键字
content = input('请输入关键字\n')
# 发送信息
s.sendto(bytes(content, encoding='utf8'), senderAddress)
# 关闭连接
recv = s.recvfrom(1024)
print(recv[0])
s.close()


