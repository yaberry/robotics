#!/usr/bin/env python

from sense_hat import SenseHat
import time
import motors_wrapper as mw
import motion_tools as mt
import communication_tools as ct
import ranger_thread as rt
import logger as l
import os
import sys
import pigpio
#import RPi.GPIO as GPIO
import ConfigParser


pi = pigpio.pi()
if not pi.connected:
   exit()

ordre=sys.argv[1]
parameter=float(sys.argv[2])

import ConfigParser

# New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each
config = ConfigParser.ConfigParser()
config.read('/home/pi/ybot/ybot.cfg')

print config.get('Motors', 'MLA')  # -> "Python is fun!"
print config.get('Ranger', 'TRIG')  # -> "Life is hard!"

Tolerance = 5
LinearTolerance=2

sense = SenseHat()
#sense.set_imu_config(True, False, False)  # magnet only
sense.set_imu_config(True, True, True)

#motors pins
MLA=5 #GRIS pin 29 M2 IN1
MLB=6 #BLANC pin 31 M2 IN2
MRA=16 #JAUNE pin 36 M1 IN1
MRB=26 #ORANGE pin 37 M1 IN2

#telemeter pins
TRIG = 17 #17 en pin
ECHO = 27 #27 en pin

#derive compensation
COMPENSATION_LEFT=1
COMPENSATION_RIGHT=1

mymotors = mw.Motors(pi, MRA, MRB, MLA, MLB, COMPENSATION_LEFT, COMPENSATION_RIGHT)

# Creation des threads
#thread_telemeter = tw.Telemeter(TRIG,ECHO)
myranger = rt.ranger_thread(pi, TRIG, ECHO, 0.3)
#thread_logger = l.Logger(sense, myranger)
# Lancement des threads
myranger.start()
#thread_logger.start()

try:
	print("waiting initialization sensors")
	time.sleep(2)
	
	if ordre=="forward":
		Duration=parameter
		#front
		cap=round(sense.get_compass(),0)
		startcap=cap	
		t=time.time()
		while time.time() < t+Duration:
			ct.setcolor(sense,"forward")	
			mt.forwardto(sense,mymotors,LinearTolerance,cap,myranger)
		mymotors.stop()
		ct.setcolor(sense,"none")
		time.sleep(1)
	
	if ordre=="rotateby":
		deg=parameter
		#rotate 180
		ct.setcolor(sense,"turningby")
		mt.turnby(sense,mymotors,Tolerance,deg)
		mymotors.stop()
		ct.setcolor(sense,"none")
		time.sleep(1)
	
	if ordre=="rotateto":
		deg=parameter	
		#take initial pos
		ct.setcolor(sense,"turningto")
		mt.turnto(sense,mymotors,Tolerance,deg)
		mymotors.stop()
		ct.setcolor(sense,"none")
	
	if ordre=="rangertest":
		while True:
			print(myranger.get_distance())
			time.sleep(0.1)

	if ordre=="log":
		while True:
			a=0

	mymotors.stop()
        sense.clear(0,0,0)
        #thread_telemeter.stop()
	myranger.stop()
	#myranger.cancel()
        #thread_logger.stop()
	#GPIO.cleanup()
        sys.exit()

except KeyboardInterrupt:
	mymotors.stop()
	sense.clear(0,0,0)
	myranger.stop()
	#myranger.cancel()
	#thread_telemeter.stop()
	#thread_logger.stop()
	#GPIO.cleanup()
	sys.exit()		

