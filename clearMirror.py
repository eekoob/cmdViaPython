import os
import time

while True:

	cmd = "eventmgr stats queue daemon.mirrord.resourceChange"
	f = os.popen(cmd)
	tempOut = f.read()
	out=tempOut.split()
	queueAmount = int(out[11])

	if queueAmount>10000 and out[10]=="daemon.mirrord.resourceChange":
		os.popen("/root/den/./mq-drain") # Execute drain script

	time.sleep(900) #check every 15 Minutes