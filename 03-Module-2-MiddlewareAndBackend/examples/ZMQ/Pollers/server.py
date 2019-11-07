#A simple script to request data from publishers.
#Shows the use of pollers. Pollers are used to constantly lookout for messages arriving in the socket.
#Event poller used here constantly listens to the socket and prints it as it has some new event arriving in the socket.

import zmq
import time
from random import *


def main():

    context = zmq.Context()
    socket= context.socket(zmq.REQ)
    socket.bind("tcp://127.0.0.1:5200")
    poller=zmq.Poller()#instantiating a zmq poller
    poller.register(socket, zmq.POLLIN)#registering poller for a particular socket
    while True:
        socket.send("send messages")
    	events=dict(poller.poll())#looking for new events using pollers
    	if socket in events:
            msg= socket.recv()
            print(msg)
    socket.close()

if __name__=="__main__":
	main()
