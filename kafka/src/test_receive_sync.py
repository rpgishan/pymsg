
import perftest, time, sys
from kafka.client import KafkaClient


brokerUrl = '192.168.0.170'


print 'connecting to: ', brokerUrl 

client = KafkaClient(brokerUrl, 9092)
destination = "perftest"

consumer = perftest.PerfConsumerSync(client, destination)
consumer.start()

for i in range(1, 50):
    time.sleep(10)
    print "consumer received ", consumer.rate.printRate()

consumer.stop()

sys.exit()
