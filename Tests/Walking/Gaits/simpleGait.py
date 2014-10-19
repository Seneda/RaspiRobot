from servo.moveJoints import moveJoint

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
    		break
