import sys
import pynng
import asyncio

_HOST = "host.docker.internal"
helper = "Usage:\n\tmqttpub.py <topic> <qos> <payload>"

address = f"mqtt-quic://{_HOST}:14567"

class MQTT_QUIC():
    def __init__(self, address: str) -> None:
        self.client = pynng.Mqtt_quic(address)


    async def connect(self):
        connmsg = pynng.Mqttmsg()
        connmsg.set_packet_type(1)  # 0x01 Connect
        connmsg.set_connect_proto_version(4)  # MqttV311
        # connmsg.set_connect_username("alvin")
        # connmsg.set_connect_password("alvin123")
        await self.client.asend_msg(connmsg)
        print("Connect packet sent.")

    async def publish(self, topic: str, payload: str, qos=2):
        pubmsg = pynng.Mqttmsg()
        pubmsg.set_packet_type(3)  # 0x03 Publish
        pubmsg.set_publish_topic(topic)
        pubmsg.set_publish_qos(qos)
        pubmsg.set_publish_payload(payload, len(payload))
        await self.client.asend_msg(pubmsg)
        print("Publish packet sent.", len(payload))
        await asyncio.sleep(0.5)

async def main():
    client = MQTT_QUIC(address)
    await client.connect()
    await client.publish("testtopic/123", """{"aaa": 123}""")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(helper)
        exit(0)
    try:
        asyncio.run(main())
    except pynng.exceptions.NNGException:
        print("Connection closed")
    except KeyboardInterrupt:
        # that's the way the program *should* end
        exit(0)
