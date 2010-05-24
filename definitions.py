#!/usr/bin/env python
# encoding: utf-8
"""
pentagon.py

Created by Chris Wood on 2010-05-23.
"""

import sys
import os
from math import pi, radians, degrees

class Point(object):
    '''
        This is just a basic cartesian system now. I think it will be cool to
        take a type in the future though, so like Point('polar', coords)
    '''
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
  
class Pentagon(object):
    '''
        side_length is the distance between points, and midpoint is an instance
        of the Point class with cartesian coordinates
    '''
    def __init__(self, side_length, midpoint):
        self.side_length = side_length
        self.midpoint = midpoint
        self.phi = (2 * pi)/5
    
def main():
    myPoint = Point([1,2])
    myPent = Pentagon(2, myPoint)
    print(myPent.midpoint.x)


if __name__ == '__main__':
	main()

