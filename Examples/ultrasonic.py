import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

def ping(pulse_start, pulse_end):
    """GET reading from sensor"""
    GPIO.setmode(GPIO.BCM)
    TRIG = 23
    ECHO = 18
    
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    GPIO.output(TRIG, False)
    time.sleep(1)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    if (pulse_start * pulse_end != 0):     
        distance = round((pulse_end - pulse_start) *17150, 2)
        print ("Distance: ", distance, "cm")
    
    GPIO.cleanup()
    
print ("Reading Distance \n")

while True:
    pulse_start = 0
    pulse_end = 0
    ping(pulse_start, pulse_end)


