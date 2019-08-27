#Simple script to publish data to a subscriber.
#Uses the REP messaging pattern.

import zmq
import time
from random import *

def main():

    context = zmq.Context()
    socket= context.socket(zmq.REP)
    socket.connect("tcp://127.0.0.1:5200")#Here the REP can be used to connect
    for i in range(100):
        msg= socket.recv()
        socket.send(str(i))
        print(i)
        x = randint(1,10)#generate random numbers
        time.sleep(x)
    socket.close()


if __name__=="__main__":
	main()
