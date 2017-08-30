import pika
import json
from neural_net import NeuralNet

class Main:
  def __init__(self):
    self.neural_net = NeuralNet()
    self.connection = pika.BlockingConnection(
      pika.ConnectionParameters("localhost")
    )

  def connect(self):
    channel = self.connection.channel()
    channel.queue_declare(queue="neural_net")

    channel.basic_consume(self.callback,
                          queue="neural_net",
                          no_ack=True
                         )

    print("[*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

  def callback(self, channel, method, properties, body):
    print("[x] Received %r" % body)

    parsed_body = json.loads(body)

    if isinstance(parsed_body, list):
      self.neural_net.update_training_set(body)
      self.neural_net.train()
    else:
      request = parsed_body['request']
      result = self.neural_net.predict(request)
      self.send_prediction(result)

  def send_prediction(self, result):
    print("Send %r" % result)
    channel = self.connection.channel()
    channel.queue_declare(queue="results")
    channel.basic_publish(exchange='',
                          routing_key='',
                          body=result)

main = Main()
main.connect()
