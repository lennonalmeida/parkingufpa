import paho.mqtt.publish as publish
import paho.mqtt.client as client
import sys
import time
#publish
#print("Sending 0...")
#publish.single("ledStatus", "0", hostname="macman")
#time.sleep(1)
#print("Sending 1...")
#publish.single("ledStatus", "1", hostname="macman")i

broker = "iot.eclipse.org"
brokerport = 1883
keepalive = 60
topic = "parkingtestufpa2"
def on_connect(client, userdata, flags, rc):
    	print("Connecting to broker: "+broker)
    	client.subscribe(topic)


def on_message(client, userdata, msg):
	message = str(msg.payload)
    	print("Topico: "+msg.topic+" | Message: "+message)
	if message == "ola":
		publish.single(topic, "recieved", hostname=broker)


try:
        print("Init MQTT")
       	print(topic) 

	host = client.Client()
        host.on_connect = on_connect
        host.on_message = on_message
        host.connect(broker, brokerport, keepalive)
	host.loop_forever()
except KeyboardInterrupt:
        sys.exit(0)
