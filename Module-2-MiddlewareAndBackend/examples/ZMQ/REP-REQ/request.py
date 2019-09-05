#! /usr/bin/python3

#Simple script to request from the server
#Uses the REP-REQ messaging pattern
#Simplest Hello-World to get a feel of REP-REQ

import zmq
import time

def main():

    context = zmq.Context()
    socket= context.socket(zmq.REQ)#Request socket
    socket.connect("tcp://localhost:5200")#connect to the socket
    print("Will request a message")
    try:
        while True:
            socket.send_string("Hi Can you send me the code")#send a request message
            msg=socket.recv_string()#Receive a reply back
            print(msg)
            time.sleep(2)
    except KeyboardInterrupt:
        print("W: interrupt received, stopping…")
    finally:
        socket.close()#close sockets
        context.term()#terminate the context


if __name__=="__main__":
	main()
