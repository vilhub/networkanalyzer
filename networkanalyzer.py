#!/usr/bin/env python

from networkanalysis import *
import time
import seaborn

import matplotlib.pyplot as plt
import numpy

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data[0]))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data[1]))
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    plt.draw()

if __name__ == '__main__':
    plt.ion()
    firstline,secondline = plt.plot([],[],[],[])
    plt.legend(['Received kb/sec','Wifi bandwidth Mbps'])


    timer = 0
    previousvolume = capture_received_volume()

    while timer < 1000:
        time.sleep(1)
        timer += 1

        newvolume = capture_received_volume()
        receivedkbpersec = ( newvolume - previousvolume ) / 1024
        currentbandwidth = capture_current_bandwidth()
        
        update_line(firstline, [timer, receivedkbpersec])
        update_line(secondline, [timer, currentbandwidth])

        previousvolume = newvolume

