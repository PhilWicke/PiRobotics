import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)

    time.sleep(tf)
    gpio.cleanup()

def backward(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False) 
    
    time.sleep(tf)
    gpio.cleanup()

def turnLeft(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)

    time.sleep(tf)
    gpio.cleanup()

def turnRight(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

    time.sleep(tf)
    gpio.cleanup()

def pivotRight(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)

    time.sleep(tf)
    gpio.cleanup()

def pivotLeft(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)

    time.sleep(tf)
    gpio.cleanup()

i = 5
while(i>0):
    forward(0.5)
    time.sleep(0.5)
    pivotLeft(0.9)
    forward(0.5)
    time.sleep(0.5)
    pivotRight(0.7)
    forward(1)
    time.sleep(0.5)
    pivotLeft(0.7)
    time.sleep(0.5)
    i-=1
