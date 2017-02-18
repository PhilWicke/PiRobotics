"""
Class that holds the controls for the robot.
"""
import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(4, gpio.OUT)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)

def forward(tf):
    init()
    gpio.output(4, False)
    gpio.output(17, True)
    gpio.output(27, False)
    gpio.output(22, True)

    time.sleep(tf)
    gpio.cleanup()

def backward(tf):
    init()
    gpio.output(4, True)
    gpio.output(17, False)
    gpio.output(27, True)
    gpio.output(22, False) 
    
    time.sleep(tf)
    gpio.cleanup()

def turnLeft(tf):
    init()
    gpio.output(4, False)
    gpio.output(17, True)
    gpio.output(27, False)
    gpio.output(22, False)

    time.sleep(tf)
    gpio.cleanup()

def turnRight(tf):
    init()
    gpio.output(4, False)
    gpio.output(17, False)
    gpio.output(27, False)
    gpio.output(22, True)

    time.sleep(tf)
    gpio.cleanup()

def pivotRight(tf):
    init()
    gpio.output(4, True)
    gpio.output(17, False)
    gpio.output(27, False)
    gpio.output(22, True)

    time.sleep(tf)
    gpio.cleanup()

def pivotLeft(tf):
    gpio.output(4, False)
    gpio.output(17, True)
    gpio.output(27, True)
    gpio.output(22, False)

    time.sleep(tf)
    gpio.cleanup()
