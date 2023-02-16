#! /usr/bin/python

import socket
import sys
from threading import *

hostIP = sys.argv[1]

def connScan(hostIP, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((hostIP, port))
        try:
            print("[+] Open Port " + str(port) + ",  " +  sock.recv(2048).decode())
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

def portScanner():
	for tgtIP in range(1,10000):
		t = Thread(target=connScan, args=(hostIP, tgtIP))
		t.start()

portScanner()