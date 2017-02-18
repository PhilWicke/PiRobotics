import sys
import numpy as np
from time import sleep
from collections import deque
from gyro import get_acceleration, get_rotation

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class plotterObj:

    # Constructor

    def __init__(self, maxLen):

        self.ax = deque([0.0]*maxLen)
        self.ay = deque([0.0]*maxLen)
        self.maxLen = maxLen


    def addToBuffer(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)

    def add(self, data):
        assert(len(data) == 2)

        self.addToBuffer(self.ax, data[0])
        self.addToBuffer(self.ay, data[1])

    def update(self, frameNum, a0, a1):

        try:
            acc = get_acceleration()
            data = get_rotation(acc[0],acc[1],acc[2])

            if(len(data) == 2):
                self.add(data)
                a0.set_data(range(self.maxLen), self.ax)
                a1.set_data(range(self.maxLen), self.ay)
        except KeyboardInterrupt:
            print('exiting')


        return a0,

def main():

    plotObj = plotterObj(100)

    fig = plt.figure()
    ax = plt.axes(xlim=(0,100), ylim=(-90,90))
    a0, = ax.plot([], [])
    a1, = ax.plot([], [])
    anim = animation.FuncAnimation(fig, plotObj.update,
                                   fargs=(a0,a1),
                                   interval=50)
                

    plt.show()
    print('exiting.')

if __name__ == '__main__':
    main()












        
