
import time, threading, sys

import zmq

class PerfRate:

    count = 0
    startTime = time.time()
    
    def printRate(self):
        endTime = time.time()
        period = endTime - self.startTime
        rate  = self.count / (endTime - self.startTime)
        return str(self.count) + " messages in " + str(period) + " secs ; rate=" + str(rate) + " msgs/sec"
    
    def increment(self):
        self.count += 1


class PerfProducer ( threading.Thread ):

    running = True

    def __init__(self, socket, topic, message_size):
        self.socket = socket
        self.topic = topic
        self.rate = PerfRate()
        self.message_size = message_size
        self.message = ""
        for i in xragne(message_size):
            self.message += "a"
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            self.socket.send("%s %s" % (self.topic, self.message))
            self.rate.increment()

    def stop(self):
        self.running = False

class PerfConsumerSync ( threading.Thread ):

    running = True

    def __init__(self, socket):
        self.socket = socket
        self.rate = PerfRate()
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            self.socket.recv()
            self.rate.increment()

    def stop(self):
        self.running = False
