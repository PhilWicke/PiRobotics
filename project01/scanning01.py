import time
import sys
import Tkinter as tk
import random
import numpy as np
from termcolor import colored # sudo python -m pip install termcolor
from sensor import distance
from radar import scanPlot
import controls as ct

"""
Rounding that will round to the 5 e.g. 7->5, 12->10, 14->15, 16->15 
"""
def myround(x, base=5):
    return int(base * round(float(x)/base))

"""
Function to find a repetition in the given sequence. Pattern length is 5.
Returns:    turnLen -> the number of distance measures that had to be taken to find a repetition
            if turnLen is '-1', there has been no repetition of length 5
"""
def find_pattern(seq):

    turnLen = -1 # Error code
    for x in range(len(seq)-11):
        for y in range(len(seq)-6):
            if seq[x:x+5] == seq[x+6+y:x+6+y+5]:
                guess = x+1
                turnLen = (x+6+y)-(x+1)
                patt = seq[x:x+5]
    #print(turnLen)
    #print(patt)
    return turnLen

"""
Function that takes n scans in the left pivot movement, with step duration t.
Returns a list of n distances.
"""
def takeNscans(n,t):
    if (n<=0 or t<=0):
        print("Invalid scan number or scan duration provided. See takeNscans function.")
        sys.exit()

    # Create list for distances to be measured
    distances = []
    # do a scan of n measurements towards left
    for x in range(n):
        ct.init()
        ct.pivotLeft(t)
        time.sleep(0.5)
        dist = myround(int(distance()+0.5))
        distances.append(dist)
    return distances
    

"""
Makes 60 measurements of 0.075 sec towards the left to retrieve distances
Check these distances for a pattern that will determine number of
necessary measurements for a 360deg rotation.
"""
def findTurnTime():
    
    distances = takeNscans(70, 0.075)
        
    '''
    for i in range(len(distances)-1):
        print(distances[i])
    
    distances = [10,10,15,25,25,25,15,15,15,15,15,20,20,10,5,5,5,5,5,60,60,30,30,25,25,25,30,35,35,15,15,10,10,15,15,25,25,15,15,15,15,15,15,15,10,5,5
,5,5,60,30,30,30,25,25,25,30,35]

    distances = [2,2,3,4,4,4,5,5,6,6,6,6,6,4,3,3,2,2,3,4,4,7,8]
    '''
    # look for a pattern that determines the turn duration
    turnLen = find_pattern(distances)
    if turnLen <= 0:
        # if you cant find a pattern repeat scanning process
        distances = takeNscans(70, 0.075)
        turnLen = find_pattern(distances)
        # if you still couldnt find it, exit
        if turnLen <= 0:
            print("Could not identify a stable environment.")
            sys.exit()
    # return the number of necessary measurements for an assumed 360deg scan
    return turnLen

"""
Function that takes the evalutated reasonable amount of steps for a single turn as turnDur and
turns is the number of single turns that should evaluate the distances in the surroundings.
"""
def scan(turnDur, turns):
    
    distances = np.zeros([turns, turnDur])
    
    for y in range(0,turns,1):
        distanceZ = []
        for z in range(turnDur):
            ct.init()
            ct.pivotLeft(0.075)
            time.sleep(0.5)
            dist = round(distance(),2)
            distanceZ.append(dist)
        distances[y]= distanceZ
        print("Round "+str(y+1)+" of "+str(turns)+" done.")

    # mean over all turns
    distances = np.mean(distances, axis=0)
    return distances
            
def autonomy():
    
    print("Evaluating turn time...")
    turnDur = findTurnTime()
    print("Start scanning "+ str(turnDur)+" measures.")
    distances = scan(turnDur,4)
    print("Scanning done, plotting...")
    
    #distances = [2,2,13,14,14,14,25,25,36,36,46,106,106,40,30,13,12,200,300,300,200,100,80]
    scanPlot(distances,10)
    

for z in range(1):
    autonomy()
    
