import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import controls as ct

def key_input(event):
    ct.init()
    #print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    # Define keys
    if key_press.lower() == 'w':
        ct.forward(sleep_time)
    elif key_press.lower() == 's':
        ct.backward(sleep_time)
    elif key_press.lower() == 'a':
        ct.turnLeft(sleep_time)
    elif key_press.lower() == 'd':
        ct.turnRight(sleep_time)
    elif key_press.lower() == 'q':
        ct.pivotLeft(sleep_time)
    elif key_press.lower() == 'e':
        ct.pivotRight(sleep_time)
    else:
        time.sleep(sleep_time)
        
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
