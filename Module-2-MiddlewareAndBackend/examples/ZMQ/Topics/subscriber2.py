#Simple script to recive the messages published by publisher on port 5200

import zmq

def main():

        context = zmq.Context()
        socket= context.socket(zmq.SUB)
        topic = "2"
        socket.connect("tcp://127.0.0.1:5200")#SUB has to subscribe to messages
        socket.setsockopt_string(zmq.SUBSCRIBE, topic)#This is a filter to receive messages from a particular topic
        print("I want to receive messages from the publisher under topic %s"%topic)
        try:
            while True:
                msg=socket.recv_string()#receive messages
                topic, message = msg.split()
                print(message)
        except KeyboardInterrupt:
            print("W: interrupt received, stopping…")
        finally:
            socket.close()
            context.term()

if __name__=="__main__":
	main()
