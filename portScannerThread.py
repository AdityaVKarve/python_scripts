#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:54:52 2019

@author: thatguy99
"""
#this port scanner makes use of threads to scan for open ports
import socket
import threading
from Queue import Queue

print_lock=threading.Lock()

target='pythonprogramming.net'

def portscan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        con=s.connect((target,port))
        with print_lock:
            print('port ',port,' is open!')
        con.close()
    except:
        pass
def threader():
    while True:
        worker=q.get()
        portscan(worker)
        q.task_done()
        
q=Queue()
for x in range(30):
    t=threading.Thread(target=threader)
    t.daemon=True
    t.start()
    
for worker in range(1,65000):
    q.put(worker)
q.join()
