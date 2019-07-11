import os
import datetime
import time
import sys

while True:

	cmd = "eventmgr stats queue daemon.mirrord.resourceChange"
	f = os.popen(cmd)
	tempOut = f.read()
	out=tempOut.split()
	queueAmount = int(out[11])

	if queueAmount>10000 and out[10]=="daemon.mirrord.resourceChange":
		os.popen("/root/den/./mq-drain") # Execute drain script
		print >> sys.stderr, "[ OK ] "+ str(datetime.datetime.now()) + " :  DRAINED  queueAmount = " + str(queueAmount) + "\n"
	else:
		print >> sys.stderr, "[ OK ] "+ str(datetime.datetime.now()) + " :  NOT DRAINED   queueAmount = " + str(queueAmount) + "\n"

	time.sleep(600) #check every 10 Minutes
