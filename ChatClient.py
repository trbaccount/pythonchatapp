import socket
import time 
import sys

#Connect to Server
s = socket.socket()
host = input("What is the host's ip: ")
port = input("What is the host's port: ")
s.connect((host,port))



while True:
	message = s.recv(1024)
	print(message.decode())
