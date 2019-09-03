#!/usr/bin/python3
from time import time
import datetime
#from datetime import datetime
import random
import time
import csv
import os
import zmq
import paho.mqtt.client as mqtt
broker= "127.0.0.1"#"192.168.99.100" #"192.168.1.184"#"test.mosquitto.org"
port=2000
topic = "code"

def on_message(client, userdata, message):
    print(message.payload.decode('utf-8'))

def on_connect(client, userdata, flags, rc):
    print('connected')
    client.subscribe(topic)

def main():
    mqtt.Client.connected_flag=False#create flag in class
    broker="127.0.0.1"#"test.mosquitto.org"
    client = mqtt.Client("Server")             #create new instance
    client.on_message= on_message                      #attach function to callback
    client.on_connect = on_connect
   #bind call back function
    client.loop_start()
    print("Connecting to broker ",broker)
    client.connect(broker)
    while True:
        pass

if __name__=="__main__":
	main()
