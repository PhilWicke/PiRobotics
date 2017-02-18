import RPi.GPIO as gpio
import time

"""
TODO:
Implement something that takes the distance of right sensor
distanceRight(measure)
distanceLeft(measure)
"""


def distance(measure='cm'):
    try:
        # setting up gpio pins
        gpio.setmode(gpio.BOARD)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.IN)

        # give the sensor some time to send first signal
        time.sleep(0.3)
        gpio.output(12,True)
        time.sleep(0.00001)
        gpio.output(12, False)
       
        # check response and note time
        while gpio.input(16) == 0:
            nosig = time.time()

        while gpio.input(16) == 1:
            sig = time.time()
    
        tlRight = sig - nosig
        
        # right side
        gpio.setup(18, gpio.OUT)
        gpio.setup(22, gpio.IN)
        time.sleep(0.3)
        gpio.output(18,True)
        time.sleep(0.00001)
        gpio.output(18, False)
        while gpio.input(22) == 0:
            nosig = time.time()
        while gpio.input(22) == 1:
            sig = time.time()
        tlLeft = sig - nosig

        tl = (tlRight+tlLeft)/2
        

        # use constant of sound to calculate distance
        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance        

#print(distance('cm'))

def distanceRight(measure='cm'):
    try:       
        # right side
        gpio.setup(18, gpio.OUT)
        gpio.setup(22, gpio.IN)
        
        time.sleep(0.3)
        gpio.output(18,True)
        time.sleep(0.00001)
        gpio.output(18, False)
        
        while gpio.input(22) == 0:
            nosig = time.time()
        while gpio.input(22) == 1:
            sig = time.time()
        tlLeft = sig - nosig

        tl = sig - nosig
        

        # use constant of sound to calculate distance
        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance

def distanceLeft(measure='cm'):
    try:
        # setting up gpio pins
        gpio.setmode(gpio.BOARD)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.IN)

        # give the sensor some time to send first signal
        time.sleep(0.3)
        gpio.output(12,True)
        time.sleep(0.00001)
        gpio.output(12, False)
       
        # check response and note time
        while gpio.input(16) == 0:
            nosig = time.time()

        while gpio.input(16) == 1:
            sig = time.time()
    
        tl = sig - nosig
        

        # use constant of sound to calculate distance
        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'in':
            distance = tl / 0.000148
        else:
            print('improper choice of measurement: in or cm')
            distance = None

        gpio.cleanup()
        return distance
    except:
        distance = 100
        gpio.cleanup()
        return distance
