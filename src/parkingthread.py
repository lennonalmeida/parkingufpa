##import RPi.GPIO as GPIO
import time
##import paho.mqtt.publish as publish
import threading

brokerport = 1883
keepalive = 60
broker = "test.mosquitto.org"
topic = "teste/app2"

#GPIO.setmode(GPIO.BOARD)

#TODO
# sensor = 12 #vector pra cada sensor
sensor = [True,False,True,True]
led = 40 #vector para cada led verde
led2 = 36 #vector para cada led vermelho
l1, l2 = [0,0,0,0], [0,0,0,0]
l1[0], l1[1], l1[2], l1[3] = False, False, False, False
l2[0], l2[1], l2[2], l2[3] = True, False, True, False #vector state dos leds
#vector state sensor
#vector state_before
#vector state_actual


# GPIO.cleanup()
#
# GPIO.setup(sensor[0], GPIO.IN)
# GPIO.setup(sensor[1], GPIO.IN)
# GPIO.setup(sensor[2], GPIO.IN)
# GPIO.setup(sensor[3], GPIO.IN)
#
# GPIO.setup(led[0], GPIO.OUT)
# GPIO.setup(led[1], GPIO.OUT)
# GPIO.setup(led[2], GPIO.OUT)
# GPIO.setup(led[3], GPIO.OUT)
#
#
# GPIO.setup(led2[0], GPIO.OUT)
# GPIO.setup(led2[1], GPIO.OUT)
# GPIO.setup(led2[2], GPIO.OUT)
# GPIO.setup(led2[3], GPIO.OUT)
estado, estado_ant = [0,0,0,0], [0,0,0,0]
estado_ant[0], estado_ant[1], estado_ant[2], estado_ant[3]  = False, False, False, False
estado[0], estado[1], estado[2], estado[3] = False, False, False, False
#
# GPIO.output(led[0],l2[0])
# GPIO.output(led[1],l2[1])
# GPIO.output(led[2],l2[2])
# GPIO.output(led[3],l2[3])
#
#
#
# GPIO.output(led2[0],l1[0])
# GPIO.output(led2[1],l1[1])
# GPIO.output(led2[2],l1[2])
# GPIO.output(led2[3],l1[3])
message = ['0', '0', '0', '0']

def send_data_mqtt(message):
        publish.single(topic, message, hostname=broker)
def thread_sensor(index):
    while True:
        # estado[index] = GPIO.input(sensor[index])
        estado[index] = sensor[index]

        if estado_ant[index] == False and estado[index] == True:
            l1[index] = not l1[index]
            l2[index] = not l2[index]
       	    # GPIO.output(led[index],l2[index])
       	    # GPIO.output(led2[index],l1[index])
	    if l2[index] == False:
		message[index] = str(index)+"/vermelho"
	    else:
		message[index] = str(index)+"/verde"
        time.sleep(5)
        estado_ant[index] = estado[index]
        if index == 3:
           print(message)
        time.sleep(1)
if __name__ == "__main__":
     threads = []
     for i in range(4): #i is index to vectors
         t = threading.Thread(target=thread_sensor, args=(i,))
         threads.append(t)
         t.start()
