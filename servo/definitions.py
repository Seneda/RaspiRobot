__author__ = 'seneda'
from servo.moveJoints import moveJoint, stop

class joint(object):
    def __init__(self, pin, max, min):
        self.pin = pin
        self.max = max
        self.min = min

    def move(self,start=0.25,end=0.75,time=1):
        diff = self.max-self.min
        moveJoint(self.pin,self.min+start*diff,self.min+end*diff,time)

    def stop(self):
        stop(self.pin)

class hipJoint(joint):
    def __init__(self, pin, frontmax, backmax):
        super(hipJoint).__init__(pin, frontmax, backmax)

class kneeJoint(joint):
    def __init__(self, pin, outmax, undermax):
        super(hipJoint).__init__(pin, outmax, undermax)


class leg(object):
    def __init__(self,hip,knee):
        self.hip = hip
        self.knee = knee


Legs = {'FR':(leg(hipJoint(9,150,450),kneeJoint(11,225,500))),
       'FL':leg(hipJoint(8,600,300),kneeJoint(10,250,550)),
       'BR':leg(hipJoint(5,200,550),kneeJoint(7,250,550)),
       'BL':leg(hipJoint(4,500,200),kneeJoint(6,200,500)),
       }

#Legs = [(leg(hipJoint(9,150,450),kneeJoint(11,225,500))),
#        leg(hipJoint(8,600,300),kneeJoint(10,250,550)),
#        leg(hipJoint(5,200,550),kneeJoint(7,250,550)),
#        leg(hipJoint(4,500,200),kneeJoint(6,200,500)),
#        ]