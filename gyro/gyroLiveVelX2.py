import sys
import numpy as np
from time import sleep, clock
from collections import deque
from gyro import get_acceleration

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class plotterObj:

    # Constructor

    def __init__(self, maxLen):

        self.ax = deque([0.0]*maxLen)
        self.ve = deque([0.0]*maxLen)
        self.t0 = 0
        self.maxLen = maxLen


    def addToBuffer(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)

    def add(self, data):
        assert( len(data) == 2)
        self.addToBuffer(self.ax, data[0])
        self.addToBuffer(self.ve, data[1])


    def update(self, frameNum, a0, a1):
        try:
            data = get_acceleration()
            acc  = data[0]   + 0.05 # offset
            t1   = clock()
             
            ve   = (abs(acc) * (t1-self.t0) + self.ve[0])/2

            self.t0 = t1
            
            self.add([acc,ve])
            a0.set_data(range(self.maxLen), self.ax)
            a1.set_data(range(self.maxLen), self.ve)

        except KeyboardInterrupt:
            print('exiting')


        return a0,

def main():

    plotObj = plotterObj(200)

    fig = plt.figure()
    ax = plt.axes(xlim=(0,200), ylim=(-0.15,0.1))
    a0, = ax.plot([], [], label='Acceleration',alpha=0.25)
    a1, = ax.plot([], [], label='Velocity')
    anim = animation.FuncAnimation(fig, plotObj.update,
                                   fargs=(a0,a1),
                                   interval=50)
                

    plt.legend()
    plt.show()
    print('exiting.')

if __name__ == '__main__':
    main()












        
