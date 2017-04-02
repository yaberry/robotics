#!/usr/bin/env python

import sys

r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]

def setcolor(sense,type):
	if type == "forward":
		sense.clear(o)
	if type == "backward":
                sense.clear(y)
	if type == "turningto":
                sense.clear(b)
	if type == "turningby":
                sense.clear(i)
	if type == "none":
                sense.clear(e)
	

