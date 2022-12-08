import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN)

if ((GPIO.input(4)) == 1):
    print("Light is on")
else:
    print("Light is off")
