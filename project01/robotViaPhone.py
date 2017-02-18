# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import os
        

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward():
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)

def backward():
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False) 

def turnLeft():
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)

def turnRight():
    init()
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

def pivotRight():
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

def pivotLeft():
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    
def halt():
    init()
    gpio.cleanup()
    print("Stopping...")

def endProgram():
    os.environ["unset"] = "DISPLAY"
    root.quit()
    root.destroy()


### Main method

# Forward the display to the XServer (XSDL) on phone
os.environ["DISPLAY"] = "192.168.178.72:0"
#os.environ["DISPLAY"] = "192.168.0.227:0"
os.environ["PULSE_SERVER"] = "tcp:192.168.72:4712" 
#os.environ["PULSE_SERVER"] = "tcp:192.168.0.227:4712"

# Initialize ktinker
init()
root = tk.Tk()

# Set display on fullscreen
wdh, hgt = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (wdh, hgt))
root.focus_set()

halt()

# Add buttons 
buttonForward = tk.Button(text="↑", height=4, width=8, font=("Arial",35,"bold"))
buttonForward.grid(row=0,column=1, sticky="N")

buttonBackward = tk.Button(text="↓", height=4, width=8, font=("Arial",35,"bold"))
buttonBackward.grid(row=2,column=1, sticky="S")

buttonLeft = tk.Button(text="←", height=4, width=8, font=("Arial",35,"bold"))
buttonLeft.grid(row=1,column=0, sticky="W")

buttonRight = tk.Button(text="→", height=4, width=8, font=("Arial",35,"bold"))
buttonRight.grid(row=1,column=2, sticky="E")

buttonPivotR = tk.Button(text="↻", height=4, width=8, font=("Arial",35,"bold"))
buttonPivotR.grid(row=0,column=2)

buttonPivotL = tk.Button(text="↺", height=4, width=8, font=("Arial",35,"bold"))
buttonPivotL.grid(row=0,column=0)

buttonExit = tk.Button(text="ESC", height=4, width=8, font=("Arial",35,"bold"))
buttonExit.grid(row=1,column=1)

# Bind buttons with Press and Release commands
buttonForward.bind("<ButtonPress-1>", lambda event: forward())
buttonForward.bind("<ButtonRelease-1>", lambda event: halt())

buttonBackward.bind("<ButtonPress-1>", lambda event: backward())
buttonBackward.bind("<ButtonRelease-1>", lambda event: halt())

buttonLeft.bind("<ButtonPress-1>", lambda event: turnLeft())
buttonLeft.bind("<ButtonRelease-1>", lambda event: halt())

buttonRight.bind("<ButtonPress-1>", lambda event: turnRight())
buttonRight.bind("<ButtonRelease-1>", lambda event: halt())

buttonPivotR.bind("<ButtonPress-1>", lambda event: pivotRight())
buttonPivotR.bind("<ButtonRelease-1>", lambda event: halt())

buttonPivotL.bind("<ButtonPress-1>", lambda event: pivotLeft())
buttonPivotL.bind("<ButtonRelease-1>", lambda event: halt())

buttonExit.bind("<ButtonPress-1>", lambda event: endProgram())

root.mainloop()



