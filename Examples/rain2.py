
import RPi.GPIO as GPIO 

import time 

DO = 18

GPIO.setmode(GPIO.BCM) 

GPIO.setup(DO, GPIO.IN)

while True: 
    tmp = GPIO.input(DO); 
    
    if tmp == 1: 
        print(" * Not raining *")
    if tmp == 0: 
        print (" * Raining!! *") 
       
    time.sleep(0.2) 
