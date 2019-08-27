#Client script using sockets
#Publishes 5 messages to the server
import socket
import time

host = '127.0.0.1'#Host IP address
port = 5001#port number for communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))#connecting to the servers socket
x=0
while (x<5):
    try:
        s.sendall(b'Hello')#send message
        data = s.recv(1024)#receive message
        print(data)
        time.sleep(3)
        x+=1
    except KeyboardInterrupt:
        print("Error Occured")
        time.sleep(3)
        s.close()#close connection
        #break
