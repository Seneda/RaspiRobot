__author__ = 'seneda'
from servo.moveJoints import moveJoint, stop
import time

class Joint(object):
    def __init__(self, pin, max, min):
        self.pin = pin
        self.max = max
        self.min = min

    def move(self,start=0.25,end=0.75,time=1):
        diff = self.max-self.min
        moveJoint(self.pin,self.min+start*diff,self.min+end*diff,time)

    def stop(self):
        stop(self.pin)

class HipJoint(Joint):
    def __init__(self, pin, frontmax, backmax):
        super(HipJoint,self).__init__(pin, frontmax, backmax)

class KneeJoint(Joint):
    def __init__(self, pin, outmax, undermax):
        super(KneeJoint,self).__init__(pin, outmax, undermax)


class Leg(object):
    def __init__(self,hip,knee):
        self.hip = hip
        self.knee = knee


legs = {'FR':(Leg(HipJoint(9,150,450),KneeJoint(11,225,500))),
       'FL':Leg(HipJoint(8,600,300),KneeJoint(10,250,550)),
       'BR':Leg(HipJoint(5,200,550),KneeJoint(7,250,550)),
       'BL':Leg(HipJoint(4,500,200),KneeJoint(6,200,500)),
       }



class Robot(object):
    def __init__(self, legs):
        self.legs = legs

    def stand(self,start=0.8,stop=0.2, time = 0.1):
        for l in self.legs.values():
            l.knee.move(start,stop,time)

    def simpleStep(self):
        for l in self.legs.values():
            l.hip.move(0.5,0.5,0.01)
            l.knee.ove(0.3,0.3,0.01)
        for l in [self.legs['FR'],self.legs['BL']]:
            l.knee.move(0.3,0.8,0.01)
            l.hip.move(0.5,0.8,0.01)
        time.sleep(1)
        for l in [self.legs['FR'],self.legs['BL']]:
            l.knee.move(0.8,0.3,0.01)
            l.hip.move(0.8,0.5,0.01)




    def stop(self):
        for l in self.legs.values():
            l.knee.stop()
            l.hip.stop()


    def step(self):


robot = Robot(legs)
#Legs = [(leg(hipJoint(9,150,450),kneeJoint(11,225,500))),
#        leg(hipJoint(8,600,300),kneeJoint(10,250,550)),
#        leg(hipJoint(5,200,550),kneeJoint(7,250,550)),
#        leg(hipJoint(4,500,200),kneeJoint(6,200,500)),
#        ]