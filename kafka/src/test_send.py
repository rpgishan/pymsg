
import perftest, time, sys
from kafka.client import KafkaClient


brokerUrl = '192.168.0.170'
message_size = 256
if(len(sys.argv) == 2):
    message_size = int(sys.argv[1])

print 'connecting to: ', brokerUrl 

client = KafkaClient(brokerUrl, 9092)
destination = "perftest"

producer = perftest.PerfProducer(client, destination, message_size)
producer.start()

for i in range(1, 50):
    time.sleep(10)
    print "producer sent ", producer.rate.printRate()

producer.stop()

sys.exit()
