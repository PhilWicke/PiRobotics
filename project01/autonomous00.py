import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import random
from sensor import distance

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)

    time.sleep(tf)
    gpio.cleanup()

def backward(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False) 
    
    time.sleep(tf)
    gpio.cleanup()

def turnLeft(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)

    time.sleep(tf)
    gpio.cleanup()

def turnRight(tf):
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

    time.sleep(tf)
    gpio.cleanup()

def pivotRight(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

    time.sleep(tf)
    gpio.cleanup()

def pivotLeft(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)

    time.sleep(tf)
    gpio.cleanup()
    
def check_front():

    # initialise gpio pins and check first distance
    init()
    dist = distance()

    # check if distance is below 30cm, if so change direction
    if dist < 30:
        print("Too close, distance: ", dist)
        init()
        backward(1)
        init()
        pivotRight(0.5)
        # check_back()
        dist = distance()

        # check new distance and again, if below 30cm change direction again
        if dist < 30:
            print("Too close, distance: ", dist)
            init()
            backward(1)
            init()
            pivotLeft(0.5)
            dist = distance()
            
            # check new distance and again, if below 30cm change direction again    
            if dist < 30:
                print("Too close, distance: ", dist)
                init()
                backward(1)
                init()
                pivotLeft(2)
                dist = distance()
                
                # check new distance and again, if below 30cm give up
                if dist < 30:
                    print("Too close, giving up with dist: ", dist)
                    sys.exit()
            
def autonomy():
    tf = 0.030
    x = random.randrange(0,3) # 0,1,2
    x = 0 # only forward now

    if x == 0:
        for y in range(10):
            check_front()
            init()
            forward(tf)
    elif x == 1:
        for y in range(10):
            check_front
            init()
            turnRight(tf)
    elif x == 2:
        for y in range(10):
            check_front
            init()
            turnLeft(tf)        

for z in range(10):
    autonomy()
    
