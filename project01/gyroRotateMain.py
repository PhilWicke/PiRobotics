import subprocess
import io
import time
import sys
import struct
import RPi.GPIO as gpio
import controls as ctr




# Start C script to get MPU6050 running and wait for initialisation
process = subprocess.Popen('../C_GyroReader/mstest')
time.sleep(4)
print("------------------------------------------------------------------------")


# Path of buffer file
buffDir = "../C_GyroReader/rotationBuff"

# desired rotation (90deg are 45 units)
endRot = 80
shift = -999

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
        ctr.pivotRight(0.030)

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

