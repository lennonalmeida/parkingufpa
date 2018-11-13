import paho.mqtt.publish as publish
#broker = "iot.eclipse.org"
brokerport = 1883
keepalive = 60
#topic = "parkingtestufpa"

broker = "test.mosquitto.org"
topic = "teste/app2"

def send_data_mqtt(message):
	publish.single(topic, message, hostname=broker)

#message is a array sort by the vacancy's order
for i in range(1,13,1):
	st = str(i)
	message = st+"/verde"
	print(message)
	send_data_mqtt(message)
