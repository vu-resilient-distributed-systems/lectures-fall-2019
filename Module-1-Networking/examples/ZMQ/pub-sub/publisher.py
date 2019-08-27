#A simple script to publish random numbers on port 5200, in every 2s interval
#PUB-SUB pattern is the easiest messaging pattern.

import zmq
import time
from random import *


def main():

    context = zmq.Context()
    socket= context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:5200")#PUB has to bind to an address & port
    while True:
        for i in range (0,100):
            msg = randint(1,100)#publishing random numbers every 2s
            socket.send(str(msg))#Send messages
            print(msg)
            time.sleep(2)
    socket.close()

if __name__=="__main__":
	main()
