#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys
sys.path.append('..')
import protocol_game_card_pb2 as pygm
import protocol_msgid_pb2
import protocol_errcode_pb2
import protocol_common_pb2



import tcpTk as tcpcon


def hit_tcp_gm(tcp_socket,testShow,token,donum):
    senddata = pygm.CSDrawCard()
    senddata.token = int(token)
    senddata.draw_id = 3
    senddata.draw_type = 1
    senddata.use_type = 1

    bitData = senddata.SerializeToString()
    for i in range(int(donum)):
        tcpcon.sendMsg(tcp_socket,testShow,senddata.msgid,bitData)
