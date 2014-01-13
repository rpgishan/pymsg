import sys
import zmq

port = "5560"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print "Collecting updates from server..."
socket.connect ("tcp://192.168.0.170:%s" % port)
topicfilter = "perftest"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
for update_nbr in range(10):
    string = socket.recv()
    topic, messagedata = string.split()
    print topic, messagedata
