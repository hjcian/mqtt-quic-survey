import datetime
import time

import paho.mqtt.client as mqtt

_HOST = "localhost"

# Connection success callback


def on_connect(client, userdata, flags, reason_code, properties):
    print('Connected with result code ', reason_code)
    client.subscribe('testtopic/#')

# Message receiving callback


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode('utf-8'))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Specify callback function
client.on_connect = on_connect
client.on_message = on_message

# Establish a connection
client.connect(_HOST, 1883, keepalive=60)
# Publish a message


client.loop_start()
while True:
    now = datetime.datetime.now()
    client.publish('testtopic/123',
                   payload='Hello World! It is a Python client test published at ' + now.isoformat(), qos=0)
    time.sleep(1)

client.loop_stop()
# client.loop_forever()
