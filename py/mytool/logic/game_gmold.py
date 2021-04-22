#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
sys.path.append('..')
import protocol_game_gm_pb2 as pygm
import tcpTk as tcpcon


def hit_tcp_gm(tcp_socket,testShow):
    senddata = pygm.CSGMCommand()
    senddata.token = 52741889835401216
    senddata.cmd = 'additem 101 1'

    bitData = senddata.SerializeToString()
    tcpcon.sendMsg(tcp_socket,testShow,senddata.msgid,bitData)

