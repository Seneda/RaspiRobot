__author__ = 'seneda'
from servo.moveJoints import moveJoint, stop
import time

class Joint(object):
    def __init__(self, pin, max, min):
        self.pin = pin
        self.max = max
        self.min = min
        self.pos = 0.5


    def move(self,end=0.75,time=1):
        diff = self.max-self.min
        start = self.pos
        moveJoint(self.pin,self.min+start*diff,self.min+end*diff,time)
        self.pos = end

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

    def stand(self,stop=0.5, time = 0.1):
        for l in self.legs.values():
            l.knee.move(stop,time)
            l.knee.move(stop,time)

    def centre(self,k0,h0,t=0.1):
        for l in self.legs.values():
            l.hip.move(h0,t)
            l.knee.move(k0,t)

    def sit(self):
        for l in [self.legs['BR'],self.legs['BL']]:
            l.hip.move(0.8,0.1)
            l.knee.move(0.8,0.1)

    def unsit(self):
        for l in [self.legs['BR'],self.legs['BL']]:
            l.hip.move(0.5,0.1)
            l.knee.move(0.5,0.1)

    def simpleStep(self,t=0.1):
        for l in self.legs.values():
            l.hip.move(0.5,t)
            l.knee.move(0.3,t)
        time.sleep(0.5)

        for l in [self.legs['FR'],self.legs['BL']]:
            l.hip.move(0.8,t)
            l.knee.move(0.8,t)
        for l in [self.legs['FL'],self.legs['BR']]:
            l.hip.move(0.2,t)


        for l in [self.legs['FR'],self.legs['BL']]:
            l.knee.move(0.3,t)
            l.hip.move(0.2,t)
        for l in [self.legs['FL'],self.legs['BR']]:
            l.hip.move(0.8,t)

        time.sleep(0.5)

        for l in [self.legs['FL'],self.legs['BR']]:
            l.hip.move(0.8,t)
            l.knee.move(0.8,t)
        for l in [self.legs['FR'],self.legs['BL']]:
            l.hip.move(0.2,t)



        for l in [self.legs['FL'],self.legs['BR']]:
            l.hip.move(0.5,t)
            l.knee.move(0.3,t)
        for l in [self.legs['FR'],self.legs['BL']]:
            l.hip.move(0.5,t)

    def simpleCreep(self,t=0.1,k0=0.25,h0=0.5,height=0.3,reach=0.3):
#1
        self.legs['FR'].knee.move(k0+height,t)

#2
        self.legs['FR'].hip.move(h0+reach,t)
        self.legs['FL'].hip.move(h0-reach,t)
        self.legs['BR'].hip.move(h0-reach,t)
        self.legs['BL'].hip.move(h0-reach,t)
#3
        self.legs['FR'].knee.move(k0,t)

#4
        self.legs['FL'].knee.move(k0+height,t)
        self.legs['FL'].hip.move(h0+reach,t)
        self.legs['FL'].knee.move(k0,t)
#5
        self.legs['BL'].knee.move(k0+height,t)
        self.legs['BL'].hip.move(h0+reach,t)
        self.legs['BL'].knee.move(k0,t)

        self.legs['BR'].knee.move(k0+height,t)
        self.legs['BR'].hip.move(h0+reach,t)
        self.legs['BR'].knee.move(k0,t)

        self.legs['FR'].hip.move(h0-reach,0.1)
        self.legs['FL'].hip.move(h0-reach,0.1)
        self.legs['BR'].hip.move(h0-reach,0.1)
        self.legs['BL'].hip.move(h0-reach,0.1)



    def stop(self):
        for l in self.legs.values():
            l.knee.stop()
            l.hip.stop()


    def drag(self,steps=1):
        for i in range(steps):
            self.sit()
            time.sleep(1)
            self.unsit()
            self.stand(stop=0.25)



robot = Robot(legs)
#Legs = [(leg(hipJoint(9,150,450),kneeJoint(11,225,500))),
#        leg(hipJoint(8,600,300),kneeJoint(10,250,550)),
#        leg(hipJoint(5,200,550),kneeJoint(7,250,550)),
#        leg(hipJoint(4,500,200),kneeJoint(6,200,500)),
#        ]