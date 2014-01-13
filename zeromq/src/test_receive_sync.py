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

import sys, time, threading, perftest

import zmq

port = "5560"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect ("tcp://192.168.0.170:%s" % port)
topicfilter = "perftest"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

consumer = perftest.PerfConsumerSync(socket)
consumer.start()

for i in range(1, 50):
    time.sleep(10)
    print "consumer received ", consumer.rate.printRate()

consumer.stop()
