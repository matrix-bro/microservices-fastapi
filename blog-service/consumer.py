import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='blog')

def callback(ch, method, properties, body):
    print("Received in Blog Service")
    print(body)

channel.basic_consume(queue='blog', on_message_callback=callback)

print("Started Consuming in Blog Service")

channel.start_consuming()

channel.close()