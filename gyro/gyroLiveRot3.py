import sys
import numpy as np
import time
from collections import deque
from gyro import get_acceleration, get_rotation, get_rotation3

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class plotterObj:

    # Constructor

    def __init__(self, maxLen):

        self.lastT = time.clock()
        self.refRot = 0             # reference rotation
        
        self.ax = deque([0.0]*maxLen)
        self.ay = deque([0.0]*maxLen)
        self.az = deque([0.0]*maxLen)
        self.maxLen = maxLen


    def addToBuffer(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)

    def add(self, data):
        assert(len(data) == 3)

        self.addToBuffer(self.ax, data[0])
        self.addToBuffer(self.ay, data[1])
        self.addToBuffer(self.az, data[2])

    def update(self, frameNum, a0, a1, a2):

        try:
            elapsedT = time.clock() - self.lastT
            self.lastT = time.clock()
            
            acc = get_acceleration()
            print(acc[2])
            data = get_rotation3(acc[0],acc[1],acc[2], elapsedT, self.refRot)
            self.refRot = data[2]
            
            if(len(data) == 3):
                self.add(data)
                a0.set_data(range(self.maxLen), self.ax)
                a1.set_data(range(self.maxLen), self.ay)
                a2.set_data(range(self.maxLen), self.az)
        except KeyboardInterrupt:
            print('exiting')


        return a0,

def main():

    plotObj = plotterObj(100)

    fig = plt.figure()
    ax = plt.axes(xlim=(0,100), ylim=(-90,90))
    a0, = ax.plot([], [])
    a1, = ax.plot([], [])
    a2, = ax.plot([], [])
    anim = animation.FuncAnimation(fig, plotObj.update,
                                   fargs=(a0,a1,a2),
                                   interval=50)
                

    plt.show()
    print('exiting.')

if __name__ == '__main__':
    main()












        
