#Simple script to request from the server
#Uses the REP-REQ messaging pattern
#Simplest Hello-World to get a feel of REP-REQ

import zmq
import time

def main():

    context = zmq.Context()
    socket= context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5200")
    for i in range(10):
        socket.send_string("Hello")
        msg=socket.recv_string()
        print(msg)
        time.sleep(2)
    socket.close()


if __name__=="__main__":
	main()
