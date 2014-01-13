import zmq
import random
import sys
import time

port = "5559"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://192.168.0.170:%s" % port)
publisher_id = random.randrange(0,9999)
while True:
    topic = "perftest"
    messagedata = "server#%s" % publisher_id
    print "%s %s" % (topic, messagedata)
    socket.send("%s %s" % (topic, messagedata))
    time.sleep(1)

