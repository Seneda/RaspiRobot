from servo.moveJoints import moveJoint, stop

def centre(i):
    moveJoint(i, 300, 400, 2)




while True:
    try:
        moveJoint(4,300,600,1)
        moveJoint(5,300,600,1)
        moveJoint(8,300,600,1)
        moveJoint(9,300,600,1)

        moveJoint(4,600,300,1)
        moveJoint(5,600,300,1)
        moveJoint(8,600,300,1)
        moveJoint(9,600,300,1)
    except KeyboardInterrupt:
        for i in [4,5,6,7,8,9,10,11]:
            stop(i)

