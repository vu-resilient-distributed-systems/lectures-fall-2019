#A simple script to reply for a request made by the client
#Uses the REP-REQ messaging pattern

import zmq
import time
from random import *


def main():

    context = zmq.Context()
    socket= context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5200")#Here REp is used to bind
    while True:
        msg= socket.recv()
        print(msg)
        time.sleep(1)
        socket.send("world")
    socket.close()

if __name__=="__main__":
	main()
