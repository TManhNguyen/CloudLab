import time

import RPi.GPIO as GPIO 
no_rain = 18
GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(no_rain, GPIO.IN)

while True: 

    try:
        if(GPIO.input(no_rain)): 

            print("No Rain Detected") 

        else: 
            print("It's raining!")
            
    except RuntimeError as error: 

        print(error.args[0]) 

        time.sleep(2.0) 

        continue 

    except Exception as error: 

        sensor.exit() 

        raise error 

    time.sleep(2.0) 
