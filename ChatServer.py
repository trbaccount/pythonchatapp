import socket
import time
import sys
import threading

#Start socket at (host,port)
s = socket.socket()
host = "192.168.1.174"
port = 4444
s.bind((host,port))
s.listen(3)
