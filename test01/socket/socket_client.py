# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/17

import socket
import threading

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8888))


def read_from_server(s):
    while True:
        print(s.recv(1024).decode('UTF-8'))
        print('111')


threading.Thread(target=read_from_server, args=(sk,)).start()
while True:
    msg = input('输入消息（exit退出）：')
    if msg == 'exit' or msg is None:
        sk.close()
        break
    sk.send(msg.encode('UTF-8'))
