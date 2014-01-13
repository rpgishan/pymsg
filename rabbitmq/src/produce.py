import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters =  pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange="test_exchange", exchange_type="direct",
                         passive=False, durable=True, auto_delete=False)

print("Sending text message")
channel.basic_publish('test_exchange', 'standard_key', 'Message to standard_key',
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=1))

connection.close()

