import random
import socket


connectTime = 1000
g_socketList = []


for i in range(connectTime):
    c = socket.socket()
    c.connect(('127.0.0.1', 9887))
    g_socketList.append(c)
while True:
    for g in g_socketList:
        g.send(random.randint(1,9999))


