import redis
import sys

r = redis.Redis("192.168.0.170")

ps_obj=r.pubsub()
ps_obj.subscribe("perftest")

while(1):
    try:
        item = next(ps_obj.listen())
        print item['data']
    except redis.exceptions.ConnectionError:
        ps_obj=r.pubsub()
        ps_obj.subscribe("perftest")
    except ValueError:
        pass      # or whatever

