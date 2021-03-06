#!/usr/bin/python
import smbus
import math
import sys

def read_byte(reg):
    return bus.read_byte_data(address, reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address,reg+1)
    value = ( h << 8 ) +l
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) +1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1) # Revision 2 else SMBus(0)
address = 0x68 # via i2cdetect -> i2cget -y 1 0x68 0x75 (1 for Revision 2)

# activate to address the module
bus.write_byte_data(address, power_mgmt_1, 0)

while(True):
    offset = 0.07
    acc_xout = read_word_2c(0x3b)
    acc_xout = (acc_xout / 16384.0)+offset
    sys.stdout.write("\rAcceleration on x-axis: %.1f" % abs(acc_xout))
    sys.stdout.flush()
