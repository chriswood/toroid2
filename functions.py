#!/usr/bin/env python
# encoding: utf-8
"""
functions.py

Created by Chris Wood on 2010-07-05.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from definitions import Pentagon, Point

#Given a midpoint, and a side length, draw a pentagon on a graph
def main():
    #First calculate coordinates
    midpoint = Point([0,0])
    side_length = 5
    pentagon = Pentagon(side_length, midpoint)
    vertices = pentagon.find_vertices()
    for point in vertices:
        print(point)

if __name__ == '__main__':
	main()

