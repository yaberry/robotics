#!/usr/bin/env python

#TRIG = 17 #17 en BCM
#ECHO = 27 #27 en BCM

import sys
from threading import Thread
import ranger_wrapper as rw
import time
import pigpio

class ranger_thread(Thread):

    def __init__(self,pi, t, e,frequence=0.5):
        Thread.__init__(self)
	self.frequence=frequence
        self.ranger = rw.ranger(pi, t, e)
	self.dis = 111222333
	self.running = True
    		
    def stop(self):
        self.running = False

    def distance(self):
	self.ranger.trig()
        time.sleep(0.1)
        return self.ranger.read()
        
    def get_distance(self):
	return self.dis

    def run(self):
	while self.running:
		self.dis = self.distance()
		#sys.stdout.write("Distance " + str(round(self.dis,2)) + "\n")
                #sys.stdout.flush()
		time.sleep(self.frequence)
	self.ranger.cancel()
    
