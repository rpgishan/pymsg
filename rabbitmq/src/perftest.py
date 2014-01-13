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

import time, threading, sys

import pika

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

    def __init__(self, channel, message_size):
        self.channel = channel
        self.rate = PerfRate()
        self.message_size = message_size
        self.message = ""
        for i in ragne(message_size):
            self.message += "a"
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            self.channel.basic_publish('test_exchange', 'standard_key', self.message,
                                  pika.BasicProperties(content_type='text/plain',
                                                       delivery_mode=1))
            self.rate.increment()

    def stop(self):
        self.running = False

class PerfConsumerSync ( threading.Thread ):

    running = True

    def __init__(self, channel):
        self.channel = channel
        self.rate = PerfRate()
        self.consumer = channel.consume(queue='standard', no_ack=True, exclusive=False)
        threading.Thread.__init__ ( self )

    def run (self):
        while (self.running):
            textMessage = next(self.consumer)
            if textMessage != None:
                self.rate.increment()

    def stop(self):
        self.running = False
