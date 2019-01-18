# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/17
"""
cs = socket() # 创建客户端套接字
cs.connect() # 尝试连接服务器
comm_loop: # 通信循环
    cs.send()/cs.recv() # 对话（发送/接收）
cs.close() # 关闭客户端套接字

"""
import socket
import threading

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8888))


def read_from_server(s):
    try:
        while True:
            print(s.recv(1024).decode('UTF-8'))
            print('111')
    except Exception as e:
        print("error exit!")


threading.Thread(target=read_from_server, args=(sk,)).start()
while True:
    msg = input('输入消息（exit退出）：')
    if msg == 'exit' or msg is None:
        break
    sk.send(msg.encode('UTF-8'))
sk.close()
