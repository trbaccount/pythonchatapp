import socket
import time 
import sys

#Connect to Server
s = socket.socket()
host = "192.168.1.174"
port = 4444
s.connect((host,port))


while True:
	message = s.recv(1024)
	print(message.decode())
