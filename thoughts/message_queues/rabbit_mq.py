import time
import pika


class RabbitMQ:
    prefix = 'rabbitmq'

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def publish(self, topic, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.exchange_declare(exchange=topic, exchange_type='fanout')
        channel.basic_publish(exchange=topic, routing_key='', body=message)
        connection.close()

    def consume(self, topic, handler):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port, connection_attempts=8, retry_delay=8))

        if connection is None:
            print(f'Failed to connect to mq({self.host}:{self.port})')
            raise ConnectionError(f'Failed to connect to mq({self.host}:{self.port})')

        channel = connection.channel()
        channel.exchange_declare(exchange=topic, exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=topic, queue=queue_name)

        def callback(channel, method, properties, body):
            handler(body)

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
