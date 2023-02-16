#! /usr/bin/python

import socket
import sys

socket.setdefaulttimeout(1)
sock = socket.socket()
hostIP = sys.argv[1]
portNumber = int(sys.argv[2])

def connScan(hostIP, port):
    if sock.connect_ex((hostIP, port)):
        print("Port %d is closed." % port)
    else:
        print("Port %d is open." % port)
    sock.close()

def portScanner(port):
	connScan(hostIP, portNumber)

portScanner(portNumber)