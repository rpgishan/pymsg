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

import perftest, time, sys
from pyactivemq import ActiveMQConnectionFactory

brokerUrl = 'tcp://localhost:61616?wireFormat=openwire'

if(len(sys.argv) == 2 and sys.argv[1] == 'stomp'):
    brokerUrl = 'tcp://localhost:61613?wireFormat=stomp'

print 'connecting to: ', brokerUrl 

factory = ActiveMQConnectionFactory(brokerUrl)
conn = factory.createConnection()
session = conn.createSession()
destination = session.createQueue("perftest")



producer = perftest.ScaleProducer(factory)
producer.start()

for i in range(1, 100):
    time.sleep(10)
    print "producer created ", producer.rate.count, " queues"

producer.stop()
producer.shutdown()

conn.close()

sys.exit()
