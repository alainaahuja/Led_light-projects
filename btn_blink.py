from tkinter import*
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

window=Tk()

number=Entry(window, text="")
number.pack()

def blink():
    print('alaina')
    if number.get()=='1':
        print('yogi')
        GPIO.output(40, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(40, GPIO.LOW)
    
    if number.get()=='2':
        GPIO.output(16, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(16, GPIO.LOW)

go=Button(window, text='GO!', command= blink)
go.pack()

    
window.mainloop()
    