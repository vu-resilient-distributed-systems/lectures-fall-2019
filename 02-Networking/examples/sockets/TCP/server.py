#Server script
import socket
import time

host = '127.0.0.1'#Host IP address
port = 5001#port number for communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Creating socket
s.bind((host, port))#Binding to a socket
print("host:%sport:%d"%(host,port))
s.listen(1)
conn, addr = s.accept()#Accept connection
while True:
    try:
        data = conn.recv(1024)#Reveive message from client
        if not data: break
        print(data)
        conn.sendall(b'Hello')#Send message to server
    except KeyboardInterrupt:
        print("Error Occured")
        time.sleep(3)
        conn.close()#close connection
        #break
