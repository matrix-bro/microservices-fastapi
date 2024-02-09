import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) 
channel = connection.channel()

channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    print("Received in callback")
    print(body)

channel.basic_consume(queue='test', on_message_callback=callback)

print("Started Consuming")

channel.start_consuming()

channel.close()