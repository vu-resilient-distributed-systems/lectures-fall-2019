import socket
import time

host = '127.0.0.1'#Host IP address
port = 7778#port number for communication
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))#binding to port
print("host:%sport:%d"%(host,port))

while True:
    try:
        message, address = s.recvfrom(1024)
        if not message: break
        print(message)
    except Exception as error:
        print("Error Occured",error)
        break
