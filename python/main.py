import datetime
import threading
import time

import paho.mqtt.client as mqtt

# _HOST = "localhost"
_HOST = "host.docker.internal"


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


def publish_message():
    while True:
        now = datetime.datetime.now()
        client.publish('testtopic/123',
                       payload='Hello World! It is a Python client test published at ' + now.isoformat(), qos=0)
        time.sleep(1)


# Start the background thread to publish messages
publish_thread = threading.Thread(target=publish_message)
publish_thread.start()

client.loop_forever(retry_first_connection=True)
