#!/usr/bin/env python

import sys

DutyTurnH=120
DutyTurnM=175
DutyTurnL=200
FreqTurn=200

CorrectionDeriveFactor=0.6

Duty=128
Frequency=200

LIMIT=0 #set to 0 to unable obstacle detection

#calcul borne max du cap
def maxcap(c,t):
        #input cap et tolerance
        r=c+t
        if (r>360):
                r=r-360
        return r

#calcul borne min du cap
def mincap(c,t):
        #input cap et tolerance
        r=c-t
        if (r<0):
                r=r+360
        return r

#reourne 1 si on est dans les bornes, 0 sinon
def inbound(head,cap,tol):
        capmax = maxcap(cap,tol)
        capmin = mincap(cap,tol)
        if ( cap + tol > 360 or cap - tol < 0):
                # on deborde a droite ou a gauche #exemple cap = 355 capmin = 345 et capmax = 5 / #exemple cap = 3 capmin = 353 et ca$
                if head >= capmin or head <= capmax:
                        #le head est dans les bornes
                        res = 1
                else:
                        #le head est pas dans les bornes
                        res = 0
        else:
                # on deborde pas #exemple cap = 50 capmin = 40 et capmax = 60
                if head >= capmin and head <= capmax:
                        #le head est dans les bornes
                        res = 1
                else:
                        #le head est pas dans les bornes
                        res = 0
        return res


#tourne de x degrees par rapport au cap actuel
def turnby(sense, mymotors, tolerance, rotation):
        head = round(sense.get_compass(),0)
        cap = head + rotation
        #sys.stdout.write("head="+str(head)+" cap="+str(cap)+" try\n")
        #on depasse 360 avec la rotation, on corrige
	if cap > 360:
                cap = cap - 360
        while inbound(head, cap, tolerance) == 0:
                aa=(head+1000)-(cap+1000)
                bb=(cap+1000)-(head+1000)
                if aa > bb:
                        #sys.stdout.write("aa=" + str(aa) + " bb=" + str(bb) + " head="+str(head)+" cap="+str(cap)+" go left\n")
                        if abs(bb) > 90:
                                dt=DutyTurnH
                        if abs(bb) > 30 and bb <= 90:
                                dt=DutyTurnM
                        if abs(bb) <= 30:
                                dt=DutyTurnL
                        mymotors.turnleft(dt,FreqTurn)
                else:
                        if abs(aa) > 90:
                                dt=DutyTurnH
                        if abs(aa) > 30 and bb <= 90:
                                dt=DutyTurnM
                        if abs(aa) <= 30:
                                dt=DutyTurnL
                        #sys.stdout.write("aa=" + str(aa) + " bb=" + str(bb) + " head="+str(head)+" cap="+str(cap)+" go left\n")
                        mymotors.turnright(dt,FreqTurn)
                head = round(sense.get_compass(),0)
        mymotors.stop()

#turn to head to x
def turnto(sense, mymotors, tolerance, cap):
	head = round(sense.get_compass(),0)
	while inbound(head, cap, tolerance) == 0:
		aa=(head+1000)-(cap+1000)
                bb=(cap+1000)-(head+1000)
		#sys.stdout.write("head ko\n")
		if aa > bb:
			if abs(bb) > 90:
                               	dt=DutyTurnH
	                if abs(bb) > 30 and bb <= 90:
        	                dt=DutyTurnM
                	if abs(bb) <= 30:
                                dt=DutyTurnL
			#sys.stdout.write("go left\n")
			mymotors.turnleft(dt,FreqTurn)
		else:
			if abs(aa) > 90:
	                        dt=DutyTurnH
        	        if abs(aa) > 30 and bb <= 90:
                                dt=DutyTurnM
                      	if abs(aa) <= 30:
                               	dt=DutyTurnL
			#sys.stdout.write("go right\n")
			mymotors.turnright(dt,FreqTurn)	
		#sys.stdout.write("head: " + str(head) + " cap: " + str(cap) + "\n")
               	#sys.stdout.flush()
		head = round(sense.get_compass(),0)
        mymotors.stop()
	
def forwardto(sense, mymotors, tolerance, cap, telemeter):
	m = telemeter.get_distance()
	if LIMIT == 0 or  m > LIMIT:
		head = round(sense.get_compass(),0)
        	sys.stdout.write("Head " + str(head) + " Cap " + str(cap) + " Ranger " + str(m) + "\n")
        	sys.stdout.flush()
	
		if inbound(head, cap, tolerance) == 1:
               		mymotors.forward(Duty, Duty, Frequency, Frequency)
		else:
			aa=(head+1000)-(cap+1000)
               		bb=(cap+1000)-(head+1000)
			if aa > bb:
				#derive a droite
				mymotors.forward(round(Duty*CorrectionDeriveFactor,0), Duty, Frequency, Frequency)
				sys.stdout.write("Derive Droite " + str(aa) + "-" + str(bb) + "\n")
               			sys.stdout.flush()
			else: 	
				#derive a gauche
				mymotors.forward(Duty, round(Duty*CorrectionDeriveFactor,0), Frequency, Frequency)
				sys.stdout.write("Derive Gauche " + str(aa) + "-" + str(bb) + "\n")
               			sys.stdout.flush()
	else:
		print(m)
		sys.stdout.write("STOP " + str(m) + "/" + str(LIMIT) + "\n")
                sys.stdout.flush()


