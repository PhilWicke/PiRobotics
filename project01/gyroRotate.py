# -*- coding: utf-8 -*-
import subprocess
import io
import time
import sys
import struct
import RPi.GPIO as gpio
import controls as ctr



def rotate(angle):

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
    
    # Start C script to get MPU6050 running and wait for initialisation
    process = subprocess.Popen('../C_GyroReader/mstest')
    time.sleep(4)
    print("------------------------------------------------------------------------")


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

    try:
        while int(shift) < int(endRot):

            # move to the right (increase the rotation)
            ctr.init()

            if right:
                ctr.pivotRight(0.030)
            else:
                ctr.pivotLeft(0.030)

            # read new rotation
            f = open(buffDir, "rb")
            byte = f.read(4)
            newRot = struct.unpack('f',byte)
            newRot = newRot[0]

            shift = abs(startRot-newRot)
            
            sys.stdout.write("\rTurning = %.2f" % shift)
            sys.stdout.flush()
            f.seek(0,0)
            f.close()
    finally:
        f.close()
        process.kill()

    process.kill()
    print

