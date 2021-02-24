#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk 
from datetime import datetime
import time
#----------------------------------------------------------------------------------------------
dt=datetime.now()
window = tk.Tk()
window.title('时间工具')
window.geometry('600x320') 
var = tk.StringVar() 
gett = time.time()
t0 = tk.Text(window, bg='green', font=('Arial', 12), width=30, height=1)
t0.place(x=130, y=14, anchor='nw')
t1 = tk.Text(window, bg='green', font=('Arial', 12), width=15, height=1)
t1.place(x=440, y=14, anchor='nw')
def hit_me1():
    gett = time.time()
    dt = datetime.now()
    var.set(dt.strftime('now: %Y-%m-%d %H:%M:%S %f'))
    t0.delete(0.0,2.0)
    t0.insert('insert', var.get())
    t1.delete(0.0,2.0)
    t1.insert('insert', gett)
b1 = tk.Button(window, text='当前时间', font=('Arial', 12), width=8, height=1, command=hit_me1)
b1.place(x=10, y=10, anchor='nw')
#----------------------------------------------------------------------------------------------
t3 = tk.Text(window, bg='green', font=('Arial', 12), width=30, height=1)
t3.place(x=302, y=64, anchor='nw')
e = tk.Entry(window,bg='green',font=('Arial', 12), width=15,show = None)#显示成明文形式
e.place(x=130, y=64, anchor='nw')
time1 = 0;
def hit_me2():
    t3.delete(0.0,2.0)
    timef = float(e.get())
    global time1
    time1 = int(timef)
    timeArray = time.localtime(time1)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    t3.insert('insert', otherStyleTime)
b2 = tk.Button(window, text='转换时间', font=('Arial', 12), width=8, height=1, command=hit_me2)
b2.place(x=10, y=60, anchor='nw')
#----------------------------------------------------------------------------------------------
t4 = tk.Text(window, bg='green', font=('Arial', 12), width=30, height=1)
t4.place(x=302, y=114, anchor='nw')
e2 = tk.Entry(window,bg='green',font=('Arial', 12), width=15,show = None)#显示成明文形式
e2.place(x=130, y=114, anchor='nw')
t_sub = tk.Text(window, bg='green', font=('Arial', 12), width=15, height=1)
t_sub.place(x=130, y=144, anchor='nw')
time2 = 0;
def hit_me2():
    t4.delete(0.0,2.0)
    t_sub.delete(0.0,2.0)
    timef = float(e2.get())
    global time2
    time2 = int(timef)
    timeArray = time.localtime(time2)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    t4.insert('insert', otherStyleTime)
    t_sub.insert('insert', time2 - time1)
b3 = tk.Button(window, text='转换时间', font=('Arial', 12), width=8, height=1, command=hit_me2)
b3.place(x=10, y=110, anchor='nw')
#----------------------------------------------------------------------------------------------
t5 = tk.Text(window, bg='green', font=('Arial', 12), width=30, height=1)
t5.place(x=302, y=174, anchor='nw')
e3 = tk.Entry(window,bg='green',font=('Arial', 12), width=15,show = None)#显示成明文形式
e3.place(x=130, y=174, anchor='nw')
t_sub1 = tk.Text(window, bg='green', font=('Arial', 12), width=15, height=1)
t_sub1.place(x=130, y=204, anchor='nw')
time3 = 0;
def hit_me3():
    t5.delete(0.0,2.0)
    t_sub1.delete(0.0,2.0)
    timef = float(e3.get())
    global time3
    time3 = int(timef)
    timeArray = time.localtime(time3)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    t5.insert('insert', otherStyleTime)
    t_sub1.insert('insert', time3 - time1)
b4 = tk.Button(window, text='转换时间', font=('Arial', 12), width=8, height=1, command=hit_me3)
b4.place(x=10, y=170, anchor='nw')
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------

window.mainloop()
