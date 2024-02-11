import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='auth')

def callback(ch, method, properties, body):
    print("Received in Auth Service")
    print(body)

channel.basic_consume(queue='auth', on_message_callback=callback)

print("Started Consuming in Auth Service")

channel.start_consuming()

channel.close()