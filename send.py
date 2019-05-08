"""
Send a quick test message 
"""
import time
import json
import paho.mqtt.client as mqtt

host = 'broker.hivemq.com'
client = mqtt.Client("eccsender_client")
client.connect(host, port=1883)
client.loop_start()

#topic = 'ecc1/iot/test'
topic = 'ecc1/iot/ctrl/run/call/testcybervalve/testcommand'
payload = {'hello': 'mqtt'}

client.publish(topic, payload=json.dumps(payload), 
            qos=1, retain=False)


#time.sleep(1)
client.loop_stop()
