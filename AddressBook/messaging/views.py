from django.shortcuts import render
from django.http import JsonResponse
import pika

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')

        # Connect to RabbitMQ and send the message
        # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        connection.close()

        return JsonResponse({'status': 'Message sent!'})

    return JsonResponse({'status': 'Invalid request method'}, status=400)

def receive_message(request):
    # Connect to RabbitMQ and get the messages
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    messages = []

    method_frame, header_frame, body = channel.basic_get(queue='hello', auto_ack=True)
    while method_frame:
        messages.append(body.decode())
        method_frame, header_frame, body = channel.basic_get(queue='hello', auto_ack=True)

    connection.close()

    return JsonResponse({'messages': messages})
