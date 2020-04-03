# -*- encoding: utf-8 -*-
# 文件名：TPC client.py
import socket
import sys

# 获取主机名
host = socket.gethostname()
host = '127.0.0.1'
# 设置端口号
port = 8282
print(host)
# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务， 指定主机和端口
s.connect((host, port))

while True:
    msgsend = input(">>").strip()
    if msgsend:
        # 发送数据
        s.send(msgsend.encode('utf-8'))
    else:
        break

    # 接收小于 1024 字节的数据
    msg = s.recv(1024)
    print(msg.decode('utf-8'))

# 关闭客户端
s.close()

