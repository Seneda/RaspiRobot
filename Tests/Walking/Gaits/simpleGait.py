from servo.moveJoints import moveJoint

def centre():
    moveJoint(4, 400, 400, 2)
    moveJoint(5, 400, 400, 2)
    moveJoint(8, 300, 300, 2)
    moveJoint(9, 450, 450, 2)
    moveJoint(10, 300, 500, 2)
    moveJoint(11, 300, 500, 2)
    moveJoint(6, 300, 500, 2)
    moveJoint(7, 300, 500, 2)


centre()
#while True:
#	try:	#
#		moveJoint(4,300,600,1)
#		moveJoint(5,300,600,1)
#		moveJoint(8,300,600,1)
#		moveJoint(9,300,600,1)
#
#		moveJoint(4,600,300,1)
#		moveJoint(5,600,300,1)
#		moveJoint(8,600,300,1)
#		moveJoint(9,600,300,1)
#	except KeyboardInterrupt:
 #   		break
