from servo.moveJoints import moveJoint

def centre():
    moveJoint(4, 400, 400, 1)
    moveJoint(5, 400, 400, 1)
    moveJoint(8, 400, 400, 1)
    moveJoint(9, 400, 400, 1)

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
