import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

for dancing_lights in range(2):
    for stairs in range(5):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(40, GPIO.HIGH)
        time.sleep(0.1)
    
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        time.sleep(0.1)


        

    for blink in range(5):
        GPIO.output(11, GPIO.HIGH)

        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(40, GPIO.HIGH)
        
        time.sleep(0.01)
    
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        time.sleep(0.1)
    
    
    

