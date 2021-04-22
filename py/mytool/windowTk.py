#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import redisTk as rdtk
import tcpTk as tcp
import logic.game_gm as gm

def showRedis(window,config):
    L_redis_ip = tk.Label(window, text="Redis IP", )
    L_redis_ip.place(x=10, y=50, anchor='nw')
    T_redis_ip = tk.Entry(window, bg='green', font=('Arial', 11), width=15, show=None)
    T_redis_ip.place(x=12, y=75, anchor='nw')
    T_redis_ip.insert(0, config['redis1_ip'])

    L_redis_port = tk.Label(window, text="Redis Port", )
    L_redis_port.place(x=210, y=50, anchor='nw')
    T_redis_port = tk.Entry(window, bg='green', font=('Arial', 11), width=8, show=None)
    T_redis_port.place(x=212, y=75, anchor='nw')
    T_redis_port.insert(0, config['redis1_port'])

    L_redis_pw = tk.Label(window, text="Redis PassWord", )
    L_redis_pw.place(x=310, y=50, anchor='nw')
    T_redis_pw = tk.Entry(window, bg='green', font=('Arial', 11), width=8, show=None)
    T_redis_pw.place(x=312, y=75, anchor='nw')
    T_redis_pw.insert(0, int(config['redis1_pw']))


def windowTk(window,config):
    testShow = tk.StringVar()
    def Button_1_frame(event):
        testShow.set('调试工具')
    frame_b1 = tk.Frame(window, width=600, height=600)
    frame_b1.bind("<Button-1>", Button_1_frame)
    frame_b1.pack()

    testShow.set('调试工具')
    L_test = tk.Label(window,font=('Arial', 15),textvariable = testShow)
    L_test.place(x=300, y=15, anchor='center')

    showRedis(window, config)
    myRedis = rdtk.connRedis(config,testShow)
    b_del_redis_key = tk.Button(window, text='删除 redis', font=('Arial', 12), width=8, height=1,command=lambda:rdtk.hitDelRedis(myRedis, "del_redis_key.cfg", testShow))
    b_del_redis_key.place(x=10, y=100, anchor='nw')

    # --测试 按钮-------------------------------------------------------------------------------
    def hit_test1():
        testShow.set('测试按钮1')
    b1 = tk.Button(window, text='测试按钮1', font=('Arial', 12), width=8, height=1, command=hit_test1)
    b1.place(x=10, y=550, anchor='nw')
    # ----------------------------------------------------------------------------------------------

    # --tcp test----------------------------------------------------------------------------------
    token = 52741893543493632
    T_token = tk.Entry(window, bg='green', font=('Arial', 11), width=20, show=None)
    T_token.place(x=210, y=145, anchor='nw')
    T_token.insert(0, token)
    donum = 1
    T_donum = tk.Entry(window, bg='green', font=('Arial', 11), width=4, show=None)
    T_donum.place(x=420, y=145, anchor='nw')
    T_donum.insert(0, donum)
    tcpconn = tcp.conSoc(config,testShow)
    b_tcp_gm = tk.Button(window, text='抽卡【token|次数】', font=('Arial', 12), width=16, height=1, command=lambda:gm.hit_tcp_gm(tcpconn,testShow,T_token.get(),T_donum.get()))
    b_tcp_gm.place(x=10, y=140, anchor='nw')
    # ----------------------------------------------------------------------------------------------

    # --定时器--------------------------------------------------------------------------------------
    time_step = 0
    def time_clock(time_step):
        time_step += 1
        try:
            myRedis.ping()
            testShow.set(time_step)
        except:
            showText.set('redis 连接错误')
        window.after(1000, lambda:time_clock(time_step))
    window.after(1000, lambda:time_clock(time_step))
    # ----------------------------------------------------------------------------------------------
    return testShow








