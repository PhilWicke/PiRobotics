import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread


img = imread('flatPic01.PNG')


# store coordinates
x_pts = []
y_pts = []
# create graph
fig, ax = plt.subplots()
line,   = ax.plot(x_pts, y_pts, marker='o')

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

fig.canvas.mpl_connect('button_press_event', onpick)
plt.imshow(img,alpha=0.5)
plt.show()
