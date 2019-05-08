from __future__ import print_function
import time
import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    try:
        msg = json.loads(payload)
    except ValueError:
        #not well formed json
        msg = payload
    print("message received " ,msg)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#host = 'test.mosquitto.org'
host = 'broker.hivemq.com'
client = mqtt.Client("eccrecv_client")
client.on_message=on_message        #attach function to callback
client.connect(host, port=1883)
client.loop_start()

topic = 'ecc1/iot/#'

client.subscribe(topic)

print('Listening forever.  Ctrl+C to stop')
while True: #wait forever for messages
    time.sleep(0.5)

