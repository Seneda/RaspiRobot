from numpy import linspace
from Adafruit_PWM_Servo_Driver import PWM
import time

#Legs Definition, (a,b,c) a=topservo pin b= bottom servo pin c = orientation
#leg = {"FR":(,),"FL":(,),"BR":(,),"BL":(,)}
servoMin = 250
servoMax = 500
pwm = PWM(0x40, debug=True)

def limit(pos):
	if pos < servoMin: 
		pos = servoMin
        if pos > servoMax: 
		pos = servoMax
	return pos
        
def stepsList(startpos, endpos, t):
	if startpos < endpos:
		floatsteps = linspace(startpos, endpos, t*30)
	elif startpos > endpos:
		floatsteps = linspace(startpos, endpos, t*30)
	intsteps = []
	for i in floatsteps:
		intsteps.append(int(i))
	return intsteps

def moveJoint(joint, startpos, endpos, t=5):
	startpos = limit(startpos)
	endpos = limit(endpos)
	steps = stepsList(startpos, endpos, t)
	for step in steps:
		print step, t/300.0
		pwm.setPWM(joint, 0, step)
		time.sleep(t/300.0)

moveJoint(4,300,500)
