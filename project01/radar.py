# -*- coding: utf-8 -*-
"""
Demo of bar plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt

def scanPlot(distances, threshold): 
     
    N = len(distances)
    threshold = 5
    
    # input the data
    radii = np.asarray(distances)

    theta = np.linspace(0.0, 2 *np.pi, N, endpoint=False)
    full = theta[1]+theta[len(theta)-1]
    width = np.full(N,full / N)
    piece = width[0]

    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    ax.set_theta_zero_location("N")
     
    # labelDeg = [ str(int(elem+0.5))+"°" for elem in np.degrees(theta)]
    labelDeg = []
    for elem in np.degrees(theta):
        if elem > 180: elem = -(361-elem)
        labelDeg.append(str(int(elem+0.5))+u"\u00B0")
     
    ax.set_xticklabels(labelDeg)
    ax.set_xticks(theta)

    # used to have 'max(radii)+0.1' instead of '50' for max length 
    arr1 = plt.arrow(0, 0, 0, 50, length_includes_head=True, aa=True, alpha = 0.5, width = 0.008,
                     edgecolor = 'black', facecolor = 'black', linewidth=3, zorder = 1, head_width=0.1, head_length=1)
     
    #yTickInterval = range(5,max(radii.astype(int)),5)
    # TODO: DYNAMICAL SCALING OF DISTANCES 

    # OLD ax.set_ylim([0,40])

    ax.set_ylim([0,max(distances)])
    
    # OLD yTickInterval = range(5,50,10)
    numLabels = int(max(distances)/8)
    yTickInterval = range(int(min(distances)),int(max(distances)),numLabels)
    
    ax.set_yticks(yTickInterval)
    ax.set_yticklabels([str(elem)+"cm" for elem in yTickInterval], fontsize=8)
    ax.set_rlabel_position(90)
     
    # Use custom colors and opacity
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet_r(r / float(max(distances))))
        bar.set_alpha(0.5)
       
    circle = plt.Circle((0, 0), radius=threshold, transform=ax.transData._b, color="red", alpha=0.5, fill=False, linewidth=3)
    ax.add_artist(circle)
     
    plt.show()

#scanPlot([10,30,13,12,20,5,10],5)
