import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish

brokerport = 1883
keepalive = 60
broker = "test.mosquitto.org"
topic = "teste/app2"

GPIO.setmode(GPIO.BOARD)

sensor = 12
led = 40 #verde
led2 = 36 #vermelho
l1, l2 = False, True
GPIO.cleanup()

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
estado_ant = False
estado = False
GPIO.output(led,l2)
GPIO.output(led2,l1)

##import threading
#
# def worker(num):
#     """thread worker function"""
#     print 'Worker: %s' % num
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()


def send_data_mqtt(message):
        publish.single(topic, message, hostname=broker)

if __name__ == "__main__":
	while True:
	    estado = GPIO.input(sensor)
	    print("Estado: "+str(estado)+"\tEstado anterior: "+str(estado_ant))

	    if estado_ant == False and estado == True:
	        l1 = not l1
	        l2 = not l2
        	GPIO.output(led,l2)
        	GPIO.output(led2,l1)
		if l2 == False:
			message = "1/vermelho"
		else:
			message = "1/verde"
		send_data_mqtt(message)
	        time.sleep(5)
	    estado_ant = estado
	    time.sleep(1)
