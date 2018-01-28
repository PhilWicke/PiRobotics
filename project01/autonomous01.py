import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
import random
from termcolor import colored # sudo python -m pip install termcolor
import sensor as se 
import controls as ctr


def rreplace(s,old,new,occurence):
    li = s.rsplit(old,occurence)
    return new.join(li)

def printDist(dist):
    seq = ""
    maxDist = 100
    boundary = 30
    
    for i in range(maxDist-1):
        seq += "#"
        if i == maxDist-boundary:
            seq += "|"

    if dist < boundary:
        msg = str(dist)
        seq = colored(seq, 'red')+colored(']>BOT', 'red')+colored(' TOO CLOSE: ','red')+colored(msg, 'red')
    else:  
        seq+= "]>BOT"
    seq = rreplace(seq, "#"," ",int(dist))
    sys.stdout.write("\r"+seq)
    sys.stdout.flush()
    
def check_front():

    # initialise gpio pins and check first distance
    ctr.init()
    dist = se.minDistance()
    printDist(dist)

    # check if distance is below 30cm, if so change direction
    if (dist < 30):
        #print("Too close, distance: ", dist)
        ctr.init()
        ctr.backward(1)
        ctr.init()
        ctr.pivotRight(0.65)
        dist = se.minDistance()
        printDist(dist)
        
        # check new distance and again, if below 30cm change direction again
        if (dist < 30):
            #print("Too close, distance: ", dist)
            ctr.init()
            ctr.backward(1.5)
            ctr.init()
            ctr.pivotLeft(0.65)
            dist = se.minDistance()
            printDist(dist)
            
            # check new distance and again, if below 30cm change direction again    
            if (dist < 30):
                #print("Too close, distance: ", dist)
                ctr.init()
                ctr.backward(2)
                ctr.init()
                ctr.pivotLeft(2)
                dist = se.minDistance()
                printDist(dist)
                
                # check new distance and again, if below 30cm give up
                if (dist < 30):
                    print("Too close, giving up with dist: ", dist)
                    sys.exit()
                    
            
tf = 0.04
for z in range(500):
    check_front()
    ctr.init()
    ctr.forward(tf)    
