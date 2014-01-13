import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters =  pika.ConnectionParameters('192.168.0.170', credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.exchange_declare(exchange="test_exchange", exchange_type="direct", passive=False, durable=True, auto_delete=False)
channel.queue_declare(queue="standard", auto_delete=True)
channel.queue_bind(queue="standard", exchange="test_exchange", routing_key="standard_key")
channel.basic_qos(prefetch_count=1)

consumer = channel.consume(queue='standard', no_ack=True, exclusive=False)

item = next(consumer)
print item[2]

connection.close()
