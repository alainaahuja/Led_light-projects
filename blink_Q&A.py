from tkinter import *
import RPi.GPIO as GPIO
import time

def main():
    #global A
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)

    window=Tk()
    canvas=Canvas(window, width=400, height=400, bg='white')
    canvas.pack()

    Q=canvas.create_text(20,20, text= '                                            what is 5+4?', fill='black', font= ('Helvetica', 30))

    A=Entry(window, text="")
    A.pack()
    
    go=Button(window, text='go!', command=lambda: Quizlet(A))
    go.pack()
        
    window.mainloop()


def Quizlet(A):
    if A.get()=='9':
        GPIO.output(40, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(40, GPIO.LOW)
    else:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(16, GPIO.LOW)
        
if __name__ == '__main__':
    main()


        
