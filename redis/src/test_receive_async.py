
import sys, time, threading, perftest

import redis
import sys

redisUrl = "192.168.0.170"
factory = redis.Redis(redisUrl)

queue = "perftest"

consumer = perftest.PerfConsumerSync(factory, queue)
consumer.start()

for i in range(1, 50):
    time.sleep(10)
    print "consumer received ", consumer.rate.printRate()

consumer.stop()
