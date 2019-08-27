#Server.py script which subscribes to a topic being published by the client
#Here we use free online MQTT brokers
#Try any of the three available online brokers: test.mosquitto.org, broker.hivemq.com, iot.eclipse.org
#To locally install MQTT broker use: sudo apt-get install mosquitto
#This creates a broker on your localhost (127.0.0.1)
#Use mosquitto -v to see the message communication between the client and server

import datetime
import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(message.payload.decode('utf-8'))

def main():
    broker= "iot.eclipse.org"#"127.0.0.1"
    topic="MQTT"
    mqtt.Client.connected_flag=False
    client = mqtt.Client("Server")#create an instance of client
    client.on_message= on_message
    client.loop_start()#start the loop
    print("Connecting to broker ",broker)
    client.connect(broker)#connect to broker
    while True:
        client.subscribe("MQTT")#subscribe to a required topic
    client.loop_stop()#stop the loop
    client.disconnect()#disconnect from the broker

if __name__=="__main__":
	main()
