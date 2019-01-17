# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/17

import socket
import threading

socket_list = []
addr = ('127.0.0.1', 8888)
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(addr)
sk.listen()


def read_from_client(s):
    try:
        return s.recv(1024).decode('UTF-8')
    except:
        socket_list.remove(s)


def server_target(s):
    try:
        while True:
            conn = read_from_client(s)
            print(conn)
            if conn is None:
                break
            for client_s in socket_list:
                client_s.send(conn.encode('UTF-8'))
    except Exception as e:
        print(e.strerror)


while True:
    s, addr = sk.accept()
    socket_list.append(s)
    threading.Thread(target=server_target, args=(s,)).start()
