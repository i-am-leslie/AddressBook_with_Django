import pika

# Connecting to the RabbitMQ server running in the Docker container
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

# Declaring a queue named 'hello'
channel.queue_declare(queue='hello')

# Sending a message to the 'hello' queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World you suck and take it from me !')

print(" [x] Sent 'Hello World!'")

# Closing the connection
connection.close()
