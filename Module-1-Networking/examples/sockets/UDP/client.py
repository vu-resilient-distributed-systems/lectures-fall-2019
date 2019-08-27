#Client script
import time
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
message = b'Hello'
addr = ('127.0.0.1', 7778)
x=0
while (x<5):#send 5 messages
    try:
        client_socket.sendto(message, addr)#send message
        print(message)
        x+=1
        time.sleep(3)
    except socket.timeout:
        print('REQUEST TIMED OUT')
