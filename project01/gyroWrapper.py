import subprocess
import io
import time
import sys
import struct

# Start C script to get MPU6050 running and wait for initialisation
process = subprocess.Popen('../C_GyroReader/mstest', shell=True)
time.sleep(4)
print("------------------------------------------------------------------------")


# Path of buffer file
buffDir = "../C_GyroReader/rotationBuff"

try:
    while True:
        f = open(buffDir, "rb")
        byte = f.read(4)
        rotation = struct.unpack('f',byte) 
        sys.stdout.write("\rRotation = %.2f" % rotation[0])
        sys.stdout.flush()
        f.seek(0,0)
        f.close()
finally:
    f.close()

process.kill()

