#Simple script to recive the messages published by publisher on port 5200

import zmq

def main():

        context = zmq.Context()
        socket= context.socket(zmq.SUB)
        socket.connect("tcp://localhost:5200")#SUB has to subscribe to messages
        socket.setsockopt(zmq.SUBSCRIBE, b'')#This is a filter to receive all incoming messages
        while True:
        	msg=socket.recv()#receive messages
        	print(msg)
        socket.close()


if __name__=="__main__":
	main()
