#!/usr/bin/env python

import pigpio

class Motors:

	def __init__(self,pig,pin_m1in1,pin_m1in2,pin_m2in1,pin_m2in2,comp_left,comp_right):
		
		#set pigpio
		self.pi=pig		
	
		#init pin motors
		self.MLA=pin_m2in1
		self.MLB=pin_m2in2
		self.MRA=pin_m1in1
		self.MRB=pin_m1in2

		#set compensation
		self.comp_left = comp_left
		self.comp_right = comp_right
		
		#set output mode
		self.pi.set_mode(self.MLA, pigpio.OUTPUT)
		self.pi.set_mode(self.MLB, pigpio.OUTPUT)
		self.pi.set_mode(self.MRA, pigpio.OUTPUT)
		self.pi.set_mode(self.MRB, pigpio.OUTPUT)

	def stop(self):
        	self.pi.write(self.MLA, 0)
        	self.pi.write(self.MLB, 0)
        	self.pi.write(self.MRA, 0)
        	self.pi.write(self.MRB, 0)
        	self.pi.set_PWM_dutycycle(self.MLB,0)
        	self.pi.set_PWM_dutycycle(self.MRB,0)

	def backward(self, ld, rd, lf, rf):
        	self.pi.write(self.MLA, 0)
        	self.pi.write(self.MLB, 1)
        	self.pi.write(self.MRA, 0)
        	self.pi.write(self.MRB, 1)
		self.pi.set_PWM_frequency(self.MLB,lf)
		self.pi.set_PWM_frequency(self.MRB,rf)
        	self.pi.set_PWM_dutycycle(self.MLB,ld)
        	self.pi.set_PWM_dutycycle(self.MRB,rd)

	def forward(self, ld, rd, lf, rf):
        	self.pi.write(self.MLA, 1)
        	self.pi.write(self.MLB, 1)
        	self.pi.write(self.MRA, 1)
        	self.pi.write(self.MRB, 1)
		self.pi.set_PWM_frequency(self.MLB,lf)
        	self.pi.set_PWM_frequency(self.MRB,rf)
        	self.pi.set_PWM_dutycycle(self.MLB,round(255-ld*self.comp_left,0))
        	self.pi.set_PWM_dutycycle(self.MRB,round(255-rd*self.comp_right,0))

	def turnleft(self, d, f):
        	self.pi.write(self.MLA, 0)
        	self.pi.write(self.MLB, 1)
        	self.pi.write(self.MRA, 1)
        	self.pi.write(self.MRB, 1)
		self.pi.set_PWM_frequency(self.MLB,f)
        	self.pi.set_PWM_frequency(self.MRB,f)
        	self.pi.set_PWM_dutycycle(self.MLB,255-d)
        	self.pi.set_PWM_dutycycle(self.MRB,d)

	def turnright(self, d, f):
		self.pi.write(self.MLA, 1)
		self.pi.write(self.MLB, 1)
		self.pi.write(self.MRA, 0)
		self.pi.write(self.MRB, 1)
		self.pi.set_PWM_frequency(self.MLB,f)
		self.pi.set_PWM_frequency(self.MRB,f)
		self.pi.set_PWM_dutycycle(self.MLB,d)
		self.pi.set_PWM_dutycycle(self.MRB,255-d)
