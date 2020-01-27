from tkinter import*
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

root=Tk()

def red_blink():
    GPIO.output(16, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(16, GPIO.LOW)
    print('red')
    display_area.config(bg="red")
    
def green_blink():
    GPIO.output(40, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(40, GPIO.LOW)
    print('green')
    display_area.config(bg="green")
    
red_btn=Button(root, text='red', command=red_blink)
green_btn=Button(root, text='green', command=green_blink)
red_btn.pack()
green_btn.pack()

display_area=Label(root, text="")
display_area.pack()

root.mainloop()
    





