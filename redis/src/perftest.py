import time, threading, sys

import redis
from redis.exceptions import ConnectionError

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

    def __init__(self, factory, queue, message_size):
        self.factory = factory
        self.queue = queue
        self.rate = PerfRate()
        self.message_size = message_size
        self.message = ""
        for i in xrange(message_size)
            self.message += "a"
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            self.factory.publish(self.queue, self.message)
            self.rate.increment()

    def stop(self):
        self.running = False

class PerfConsumerSync ( threading.Thread ):

    running = True

    def __init__(self, factory, queue):
        self.factory = factory
        self.queue = queue
        self.ps_obj = self.factory.pubsub()
        self.ps_obj.subscribe(self.queue)
        self.rate = PerfRate()
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            try:
                next(self.ps_obj.listen())
                self.rate.increment()
            except redis.exceptions.ConnectionError:
                self.ps_obj=self.factory.pubsub()
                self.ps_obj.subscribe(self.queue)
            except ValueError:
                pass      # or whatever

    def stop(self):
        self.running = False
