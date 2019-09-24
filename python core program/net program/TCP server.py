#  -*- encoding: utf-8 -*-
# 文件名: TCP server.py

import socket
import sys
import time

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serversocket = socket.socket()
# 获取主机名
# host = socket.gethostname()
host = '127.0.0.1'
port = 9999
print('host:',host)

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数, 超过后排队
serversocket.listen(5)


# 建立客户连接
print('服务器启动，监听客户端链接')
clientsocket, addr = serversocket.accept()
print("连接客户端地址:%s" % str(addr))

while True:
    try:
        # 接收客户端不大于1024 byte数据
        msgrev = clientsocket.recv(1024)
    except Exception:
        print('断开客户端连接', addr)

    if msgrev:
        print('客户端发送内容：', msgrev.decode('utf-8'))
    else:
        break
    msg = time.strftime("%Y-%m-%d %X")  # 获取结构化事件戳
    msg1 = '[%s]:%s' % (msg, msgrev.decode('utf-8'))

    # 发送数据
    clientsocket.send(msg1.encode('utf-8'))  # 发送消息给已链接客户端

clientsocket.close()

