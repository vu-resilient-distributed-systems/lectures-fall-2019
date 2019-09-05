#! /usr/bin/python3

#A simple script to reply for a request made by the client
#Uses the REP-REQ messaging pattern

import zmq
import time
from random import *


def main():

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5200")#Here REP is used to bind
    print("Waiting for a request")
    try:
        while True:
            msg = socket.recv_string()#Receive the request
            print(msg)
            time.sleep(1)
            socket.send_string(str(randint(1,100)))#Send the reply
    except KeyboardInterrupt:
        print("W: interrupt received, stopping…")
    finally:
        socket.close()
        context.term()

if __name__=="__main__":
	main()
