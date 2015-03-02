#!/usr/bin/env python

import os
import re

def capture_received_volume():
    """
    Returns current volume of network data received
    """

    bytes_received = 0
    re_expr = re.compile(r'\s*RX\sbytes:([0-9]+)')
    
    ifout = os.popen('ifconfig wlan0')
    for line in ifout:
        rematch = re_expr.match(line)
        if rematch:
            bytes_received = rematch.group(1)
            break
    return float(bytes_received)


def capture_current_bandwidth():
    """
    Returns current bandwidth used by wifi
    """

    bandwidth_used = 0
    re_expr = re.compile(r'\s*Bit\sRate=(\S+)')

    iwout = os.popen('iwconfig wlan0')
    for line in iwout:
        rematch = re_expr.match(line)
        if rematch:
            bandwidth_used = rematch.group(1)
            break
    return float(bandwidth_used)


if __name__ == '__main__':
    print capture_received_volume()
    print capture_current_bandwidth()
