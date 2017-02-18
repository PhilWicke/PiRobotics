# -*- coding: utf-8 -*-
import time
import subprocess
import io
import sys
import struct
import RPi.GPIO as gpio
import controls as ctr
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread



def rotate(angle, process):

    # Need to fix 90 degrees
    if angle == 180:
        angle = 179

    # counter drift due to inertia
    driftBias = 20

    # set sleep_time
    sleep_time = 0.03

    if angle == 0:
        return

    # Degree conversion
    if angle > 360:
        angle = angle % 360
    if angle < -360:
        angle = angle % -360

    if angle > 180 and angle < 360:
        angle = -(360 - angle)
    if angle < -180 and angle < -360:
        angle = 360 - angle

    # Conversion to unit angles (90°=45u)
    uAngle = angle/2

    # Path of buffer file
    buffDir = "../C_GyroReader/rotationBuff"

    # desired rotation (90deg are 45 units)
    endRot = uAngle
    right  = True
    shift = -999

    if endRot < 0:
        endRot = -(endRot)
        right = False
    
    # get start rotation value
    try:
        f = open(buffDir, "rb")
        byte = f.read(4)
        startRot = struct.unpack('f',byte)
        startRot = startRot[0]
        f.seek(0,0)
        f.close()
    finally:
        f.close()

    # endRot is in [1 to 90] interval
    # for the bias: [1 90-bias] interval
    endRot = endRot - driftBias
    if endRot <= 0:
        endRot = 1
    
    try:
        while int(shift) < int(endRot):

            # move to the right (increase the rotation)
            ctr.init()

            if right:
                ctr.pivotRight(sleep_time)
            else:
                ctr.pivotLeft(sleep_time)

            # read new rotation
            f = open(buffDir, "rb")
            byte = f.read(4)
            newRot = struct.unpack('f',byte)
            newRot = newRot[0]

            shift = abs(startRot-newRot) 
            inDeg = shift*2 + driftBias*2
            
            sys.stdout.write("\rTurning = %.2f" % inDeg)
            sys.stdout.flush()
            f.seek(0,0)
            f.close()

    finally:
        f.close()

    
def driveRoute(actionList):

    # Start C script to get MPU6050 running and wait for initialisation
    process = subprocess.Popen('../C_GyroReader/mstest')
    time.sleep(4)
    print("------------------------------------------------------------------------")

    velocity = 20 # cm / sec
    sleep_time = 0.030

    accel_bias = 0.2 

    try:
        for elem in actionList:

            angle = elem[0]
            pathLen = elem[1]

            # no bias if no distance
            if pathLen == 0:
                accel_bias = 0

            # show/start rotating process
            print "Rotating "+str(angle)+" deg."
            if angle != 0:
                angle = angle # drift bias
                rotate(angle, process)
            print 
            print "Rotating finished."

            # time = cm / (cm/sec)
            runtime = pathLen / velocity
            t0 = time.time()
            t_end = t0 + runtime + accel_bias # acceleration bias

            # counter drift to right
            counter = 1
            offStep = 34

            # show/start driving process
            print "Driving "+str(pathLen)+" cm."
            while time.time() < t_end:
                ctr.init()
                if counter % offStep == 0:
                    ctr.turnLeft(sleep_time)
                else:
                    ctr.forward(sleep_time) 
            print "Driving done."
            
    finally:
        process.kill()

def onpick(event):
    # take coordinates from event handle
    x_i, y_i = event.x, event.y
    # tranform from display data to coordinates
    x, y = ax.transData.inverted().transform([x_i, y_i])
    # store in coordinates
    x_pts.append(x)
    y_pts.append(y)
    # draw point
    line.set_xdata(x_pts)
    line.set_ydata(y_pts)
    # update plot
    fig.canvas.draw()

def distEuclidean(a,b):
    return np.sqrt(np.sum((a-b)**2))

def points2vec(p1,p2):
    return np.array([p1[0]-p2[0],p1[1]-p2[1]])

def startRoute(event):
    if (len(x_pts)<2) or (len(y_pts)<2):
        print "No path has been defined, click on at least 2 points."
        return
    if(len(x_pts) != len(y_pts)):
        print "Invalid points set up."
        return

    # calculate euclidean distance between points
    dists = np.zeros(len(x_pts)-1)
    
    for i in range(len(x_pts)-1):

        pOne = np.array([x_pts[i],y_pts[i]])
        pTwo = np.array([x_pts[i+1],y_pts[i+1]])
        dists[i] = distEuclidean(pOne,pTwo)
        print "Distance: "+str(dists[i])
        print ""
        
    # calculate vectors
    vects = np.zeros([len(x_pts),len(x_pts)])
    vects[0] = (0 , -1)  # DEFINE START VECTOR
    for i in range(len(vects)+1):

        #pOne = np.array([x_pts[i],y_pts[i]])
        #pTwo = np.array([x_pts[i+1],y_pts[i+1]])
        vects[i+1] = [x_pts[i]-x_pts[i+1],y_pts[i]-y_pts[i+1]]
 

    # calculate angle between all points
    angles = np.zeros(len(x_pts))

    
#######################################################################
"""
First point must be given -> hard code first point and draw in map
Neglect first point for driving but account for direction of start
 

"""
#######################################################################

# Load image of flat 100px = 1,00m 
img = imread('flatPic01.PNG')


# store coordinates
x_pts = []
y_pts = []


# create graph
fig, ax = plt.subplots()
line,   = ax.plot(x_pts, y_pts, marker='o')
fig.canvas.mpl_connect('button_press_event', onpick)
fig.canvas.mpl_connect('key_press_event', startRoute)
plt.imshow(img,alpha=0.5)
plt.show()


