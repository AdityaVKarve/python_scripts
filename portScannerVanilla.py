#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:54:31 2019

@author: thatguy99
"""


import socket
#this script scans through the first 26 ports to check for open ports
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server='pythonprogramming.net'
port=80
def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
        if pscan(x):
            print('Port ',x,' is open')
        else:
            print('Port ',x,' is closed')
