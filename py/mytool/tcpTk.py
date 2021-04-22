#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket as sock
import struct

def conSoc(config,testShow):
    tcp_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    try:
        tcp_socket.connect((config['gamesrv_ip'], int(config['gamesrv_port'])))
    except:
        testShow.set('TCP 连接错误')
        return
    return tcp_socket

def sendMsg(tcp_socket,testShow,msgid,SerializeData):
    datalen = len(SerializeData)
    size = datalen + 4 + 2
    sendStruct =struct.pack('>IH',size,msgid)
    senmsg = sendStruct + SerializeData
    try:
        tcp_socket.send(senmsg)
    except:
        testShow.set('TCP 连接错误')
