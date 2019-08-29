#client.py script which publishes messages under a topic.
#The client first connects itself to the online broker and publishes the messages.
#Try any of the three available online brokers: test.mosquitto.org, broker.hivemq.com, iot.eclipse.org
#To locally install MQTT broker use: sudo apt-get install mosquitto
#This creates a broker on your localhost (127.0.0.1)
#Use mosquitto -v to see the message communication between the client and server

import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def main():
    broker="iot.eclipse.org" #"127.0.0.1"#online broker
    mqtt.Client.connected_flag=False
    client = mqtt.Client("client")#create an instance of client
    client.on_connect=on_connect
    client.loop_start()
    print("Connecting to broker ",broker)
    client.connect(broker)      #connect to the online broker
    while not client.connected_flag: #wait in loop until the client connects to broker
        print("wait")
        time.sleep(1)
    print("Ready to send message")
    for i in range(0,10):
        msg= "hello"
        client.publish("MQTT",msg)#publish the messages to broker
        print(msg)
        time.sleep(5)
    client.disconnect()

if __name__=="__main__":
	main()
