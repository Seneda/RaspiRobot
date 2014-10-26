from servo.moveJoints import moveJoint, stop
import time
def centre(i):
    moveJoint(i, 300, 400, 2)

def test(i,pos):
    try:
        moveJoint(i,pos-10,pos+10,5)
    except KeyboardInterrupt:
        stop(i)

def stand(t):
        for i in [6,7,10,11]:
            moveJoint(i,200,200,1)
        time.sleep(t)
        for i in [6,7,10,11]:
            stop(i)


# try:
#     while True:
#         moveJoint(4,300,600,1)
#         moveJoint(5,300,600,1)
#         moveJoint(8,300,600,1)
#         moveJoint(9,300,600,1)
#         moveJoint(4,600,300,1)
#         moveJoint(5,600,300,1)
#         moveJoint(8,600,300,1)
#         moveJoint(9,600,300,1)
#
# except KeyboardInterrupt:
#     for i in [4,5,6,7,8,9,10,11]:
#         stop(i)

