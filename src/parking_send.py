import paho.mqtt.publish as publish
broker = "iot.eclipse.org"
brokerport = 1883
keepalive = 60
topic = "parkingtestufpa"

def send_data_mqtt(message):
	publish.single(topic, message, hostname=broker)

#message is a array sort by the vacancy's order
message = "0,0,1,0"
send_data_mqtt(message)
