import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

sensor = 12
led = 40
led2 = 36
l1, l2 = False, True
GPIO.cleanup()

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
estado_ant = False
estado = False
GPIO.output(led,l2)
GPIO.output(led2,l1)

while True:
    estado = GPIO.input(sensor)
    print("Estado: "+str(estado)+"\tEstado anterior: "+str(estado_ant))

    if estado_ant == False and estado == True:
        l1 = not l1
        l2 = not l2
        GPIO.output(led,12)
        GPIO.output(led2,l1)
        time.sleep(5)
    estado_ant = estado
    time.sleep(1)
