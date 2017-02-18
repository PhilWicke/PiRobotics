# -*- coding: utf-8 -*-
import controls as ctr
import time

import subprocess
import io
import time
import sys
import struct
import RPi.GPIO as gpio
import controls as ctr



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

    


# Start C script to get MPU6050 running and wait for initialisation
process = subprocess.Popen('../C_GyroReader/mstest')
time.sleep(4)
print("------------------------------------------------------------------------")

actionList = [(0,50),(180,50),(180,50),(180,50),(180,0)]
#actionList = [(0,100),(90,220),(90,300)]

velocity = 20 # cm / sec
sleep_time = 0.030

accel_bias = 0.2 

try:
    for elem in actionList:

        angle = elem[0]
        distance = elem[1]

        # no bias if no distance
        if distance == 0:
            accel_bias = 0

        # show/start rotating process
        print "Rotating "+str(angle)+" deg."
        if angle != 0:
            angle = angle # drift bias
            rotate(angle, process)
        print 
        print "Rotating finished."

        # time = cm / (cm/sec)
        runtime = distance / velocity
        t0 = time.time()
        t_end = t0 + runtime + accel_bias # acceleration bias

        # counter drift to right
        counter = 1
        offStep = 34

        # show/start driving process
        print "Driving "+str(distance)+" cm."
        while time.time() < t_end:
            ctr.init()
            if counter % offStep == 0:
                ctr.turnLeft(sleep_time)
            else:
                ctr.forward(sleep_time) 
        print "Driving done."
        
        
finally:
    process.kill()




