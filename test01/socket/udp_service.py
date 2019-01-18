# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/17

from socket import *
from time import ctime

HOST = ''
PROT = 9999
BUFSIZE = 1024
ADDR = (HOST, PROT)
udpSreSock = socket(AF_INET, SOCK_DGRAM)
udpSreSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSreSock.recvfrom(BUFSIZE)
    udpSreSock.sendto(('[%s] %s' % (ctime(), data.decode('UTF-8'))).encode('UTF-8'), addr)
    print('...received from and returned to: ', addr)

udpSreSock.close()
