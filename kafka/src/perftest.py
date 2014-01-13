# Copyright 2009 Dejan Bosanac <dejan@nighttale.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import threading, time, sys, signal

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer

def clean(*args):
    print "the end!"
    sys.exit(0)

for sig in (signal.SIGINT, signal.SIGTERM):
    signal.signal(sig, clean)

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
        

class PerfConsumerSync ( threading.Thread ):

    running = True

    def __init__(self, factory, destination):
        self.factory = factory
        self.destination = destination
        self.consumer = SimpleConsumer(self.factory, "test-group", self.destination)
        self.rate = PerfRate()
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            textMessage = self.consumer.get_messages(block=True, timeout=1000000)
            if (textMessage != None):
                self.rate.increment()

    def stop(self):
        self.running = False

    def start(self):
        threading.Thread.start(self)


class PerfProducer ( threading.Thread ):

    running = True

    def __init__(self, factory, destination, message_size):
        self.factory = factory
        self.destination = destination
        self.producer = SimpleProducer(factory, self.destination)
        self.rate = PerfRate()
        self.message_size = message_size
        self.message = ""
        for i in range(message_size):
            self.message += "a"
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            self.producer.send_messages(self.message)
            self.rate.increment()

    def stop(self):
        self.running = False

