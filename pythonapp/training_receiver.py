import pika
from neural_net import NeuralNet

def callback(channel, method, properties, body):
  print("[x] Received %r" % body)
  neural_net = NeuralNet(body)
  neurla_net.train()

connection = pika.BlockingConnection(
  pika.ConnectionParameters("localhost")
)

channel = connection.channel()
channel.queue_declare(queue="training")

channel.basic_consume(callback,
                      queue="training",
                      no_ack=True
                     )

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
