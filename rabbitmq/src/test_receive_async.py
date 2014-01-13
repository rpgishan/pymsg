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

import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters =  pika.ConnectionParameters('192.168.0.170', credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.exchange_declare(exchange="test_exchange", exchange_type="direct", passive=False, durable=True, auto_delete=False)
channel.queue_declare(queue="standard", auto_delete=True)
channel.queue_bind(queue="standard", exchange="test_exchange", routing_key="standard_key")
channel.basic_qos(prefetch_count=1)


consumer = perftest.PerfConsumerSync(channel)
consumer.start()

for i in range(1, 50):
    time.sleep(10)
    print "consumer received ", consumer.rate.printRate()

consumer.stop()

connection.close()
