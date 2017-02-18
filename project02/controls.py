"""
Class that holds the controls for the robot.
"""
import RPi.GPIO as gpio
import time

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
