#! /usr/bin/python

import socket
import sys
import termcolor

socket.setdefaulttimeout(1)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostIP = sys.argv[1]
portNumber = sys.argv[2]

def portScanner(port):
    if sock.connect_ex((hostIP, int(port))):
        print(termcolor.colored(("Port %d is closed." % int(port)), "red"))
    else:
        print(termcolor.colored(("Port %d is open." % int(port)), "green"))

portScanner(portNumber)
