# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/17

from socket import *

HOST = '127.0.0.1'
PROT = 9999
BUFSIZE = 1024
ADDR = (HOST, PROT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode('UTF-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode('UTF-8'))

udpCliSock.close()
