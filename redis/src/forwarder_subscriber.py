import redis
import sys

r = redis.Redis("localhost")
r.publish("perftest","test")
