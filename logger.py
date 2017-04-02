#!/usr/bin/env python

#TRIG = 11 #17 en BCM
#ECHO = 13 #27 en BCM

import sys
import time
from threading import Thread

class Logger(Thread):

    def __init__(self, s, t):
        Thread.__init__(self)
	self.running = True
	self.sense = s
	self.telemeter = t
	self.file = open("/home/pi/ybot/traces.txt", "w")
        self.file.write("begin\n")
                
    def stop(self):
        self.running = False

    def run(self):
	while self.running:
		#self.file.write("compas    : "+str(round(self.sense.get_compass(),2))+"\n")
		#self.file.write("accel raw : "+str(self.sense.accelerometer_raw)+"\n")
		#self.file.write("accel     : "+str(self.sense.accelerometer)+"\n")
		#self.file.write("gyro raw   : "+str(self.sense.gyroscope_raw)+"\n")
		#self.file.write("gyro 	    : "+str(self.sense.gyroscope)+"\n")
		#sys.stdout.write("gyro raw   : "+str(self.sense.gyroscope_raw)+"\r")
                #sys.stdout.flush()
		time.sleep(0.01)
	self.file.close()


    
