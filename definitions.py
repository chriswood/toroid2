#!/usr/bin/env python
# encoding: utf-8
"""
pentagon.py

Created by Chris Wood on 2010-05-23.
"""

import sys
import os
from math import pi, radians, degrees, sin, cos

class Point(object):
    '''
        This is just a basic 2d cartesian system now. I think it will be cool to
        take a type in the future though, so like Point('polar', coords)
    '''
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        
    def __str__(self):
        return('%s,%s' %(self.x, self.y))
  
class Pentagon(object):
    '''
        side_length is the distance between points, and midpoint is an instance
        of the Point class with cartesian coordinates.
        C1, c2, etc refer to vertices
        This draws one "on its side" so 2 vertices form a line parallel to y axis
    '''
    def __init__(self, side_length, midpoint):
        self.side_length = side_length
        self.midpoint = midpoint
        self.phi = (2 * pi)/5
        
    def __str__(self):
        return("""
************************************* 
              Pentagon
    Side length = %s, midpoint = %s     
*************************************""" %(self.side_length, self.midpoint))
        
    def find_vertices(self):
        phi = self.phi
        x = self.midpoint.x
        y = self.midpoint.y
        r = self.side_length
        c1 = Point([x + r, y])
        c2 = Point([x + r*cos(phi), y - r*sin(phi)])
        c3 = Point([x - r*cos(phi/2), y - r*sin(phi/2)])
        c4 = Point([x - r*cos(phi/2), y + r*sin(phi/2)])
        c5 = Point([x + r*cos(phi), y + r*sin(phi)])
        
        return([c1, c2, c3, c4, c5])


