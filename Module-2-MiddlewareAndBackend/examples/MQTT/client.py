from time import time
import datetime
#from datetime import datetime
import random
import time
import csv
import os
import zmq
import paho.mqtt.client as mqtt
broker= "127.0.0.1"#"192.168.99.100" #"192.168.1.184""test.mosquitto.org"
port=2000
topic = "code"

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def main():
    mqtt.Client.connected_flag=False#create flag in class
    broker="127.0.0.1"#"test.mosquitto.org"
    client = mqtt.Client("client1")             #create new instance
    client.on_connect=on_connect  #bind call back function
    client.loop_start()
    print("Connecting to broker ",broker)
    client.connect(broker)
    while not client.connected_flag: #wait in loop
        print("In wait loop")
        time.sleep(1)
    print("Main Loop")
    msg="hello"
    while True:
        client.publish(topic, msg)
        print(msg)
        time.sleep(2)

    client.disconnect()

if __name__=="__main__":
	main()

