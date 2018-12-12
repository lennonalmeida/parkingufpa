import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish
import threading

brokerport = 1883
keepalive = 60
broker = "test.mosquitto.org"
topic = "teste/app2"

GPIO.setmode(GPIO.BOARD)



message = ["0/verde", "1/verde"]


sensor = [12, 15] #vector pra cada sensor
#sensor = [True,False,True,True]
led_r = [13, 16]  #vector para cada led comunista
led_g = [7, 18] #vector para cada led maconheiro
l_red, l_green = [0,0,0,0], [0,0,0,0]
l_red[0], l_red[1], l_red[2], l_red[3] = False, False, False, False
l_green[0], l_green[1], l_green[2], l_green[3] = True, True, True, True #vector state dos leds

#GPIO.cleanup()
#
GPIO.setup(sensor[0], GPIO.IN)
GPIO.setup(sensor[1], GPIO.IN)
#GPIO.setup(sensor[2], GPIO.IN)
#GPIO.setup(sensor[3], GPIO.IN)
#
GPIO.setup(led_r[0], GPIO.OUT)
GPIO.setup(led_r[1], GPIO.OUT)
#GPIO.setup(led_r[2], GPIO.OUT)
#GPIO.setup(led_r[3], GPIO.OUT)
#
#
GPIO.setup(led_g[0], GPIO.OUT)
GPIO.setup(led_g[1], GPIO.OUT)
#GPIO.setup(led_g[2], GPIO.OUT)
#GPIO.setup(led_g[3], GPIO.OUT)
estado, estado_ant = [0,0,0,0], [0,0,0,0]
estado_ant[0], estado_ant[1], estado_ant[2], estado_ant[3]  = False, False, False, False
estado[0], estado[1], estado[2], estado[3] = False, False, False, False
#
GPIO.output(led_r[0],l_red[0])
GPIO.output(led_r[1],l_red[1])
#GPIO.output(led_r[2],l_red[2])
#GPIO.output(led_r[3],l_red[3])

#
#
GPIO.output(led_g[0],l_green[0])
GPIO.output(led_g[1],l_green[1])
#GPIO.output(led_g[2],l_green[2])
#GPIO.output(led_g[3],l_green[3])
#message = ['0', '0', '0', '0']

def sensores(index):
    ret = ""
    estado[index] = GPIO.input(sensor[index])
    print("sensor "+str(index))
    #estado[index] = sensor[index]
    print("Estado anterior: "+str(int(estado_ant[index]))+"| Estado atual: "+str(int(estado[index])))
    if estado_ant[index] == False and estado[index] == True:
        l_red[index] = not l_red[index]
        l_green[index] = not l_green[index]
        GPIO.output(led_r[index],l_red[index])
        GPIO.output(led_g[index],l_green[index])
        if l_red[index] == True:
	    #message[index] = str(index)+"/vermelho"
            ret = str(index)+"/vermelho"
        else:
            #message[index] = str(index)+"/verde"
            ret = str(index)+"/verde"
    estado_ant[index] = estado[index]
    return ret

if __name__ == "__main__":
    thread = 0
    if thread:
        threads = []
        for i in range(2): #i is index to vectors
            t = threading.Thread(target=thread_sensor, args=(i,))
            threads.append(t)
            t.start()
    else:
        while True:
            for i in range(2):
                message[i] = sensores(i)
                publish.single(topic, message[i], hostname=broker)
                time.sleep(1)
