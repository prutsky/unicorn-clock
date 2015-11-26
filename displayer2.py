#!/usr/bin/env python

#!
# Sense HAT Clock
# https://github.com/repraze/unicorn-clock
#
# Copyright 2015, - Thomas Dubosc (http://repraze.com)
# Released under the MIT license
# Converted to Sense HAT - Erwin Harkink
#

import sys
from sense_hat import SenseHat

import time

sense = SenseHat()

sense.set_rotation(180)

def getData():
	data = sys.stdin.readline().rstrip("\n").split(";")
	
	return data

while True:
	rgbm = getData()
	if rgbm:
		for y in range(8):
			for x in range(8):
				try:
					rgb=rgbm[y*8+x].split(",")
					sense.set_pixel(x,y,int(rgb[0]),int(rgb[1]),int(rgb[2]))
					#UH.set_pixel(x,y,255,0,0)
				except ValueError:
					pass
				except IndexError:
					pass

	sys.stdout.write('DONE\n')
	sys.stdout.flush()
	#time.sleep(0.04)
