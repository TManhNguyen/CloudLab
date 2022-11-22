import RPi.GPIO as GPIO 
import time 

 

PIR_input = 13				#read PIR Output 

GPIO.setwarnings(False) 

GPIO.setmode(GPIO.BOARD)		#choose pin no. system 

GPIO.setup(PIR_input, GPIO.IN)	 

while True: 

#when motion detected turn on LED 
    try:
        if(GPIO.input(PIR_input)): 

            print("True") 

        else: 
            print("False")
            
    except RuntimeError as error: 

        print(error.args[0]) 

        time.sleep(2.0) 

        continue 

    except Exception as error: 

        sensor.exit() 

        raise error 

    time.sleep(2.0) 

          

