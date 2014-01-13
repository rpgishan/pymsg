
import sys, time, threading, perftest

import redis

redisUrl = "192.168.0.170"
message_size = 256

if(len(sys.argv) == 2):
    message_size = int(sys.argv[1])

factory = redis.Redis("192.168.0.170")

queue = "perftest"

producer = perftest.PerfProducer(factory, queue, message_size)
producer.start()

for i in range(1, 50):
    time.sleep(10)
    print "producer sent ", producer.rate.printRate()

producer.stop()

