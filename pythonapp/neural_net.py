import tensorflow as tf
import json

class NeuralNet
  def __init__(self, training_data):
    self.training_data, self.training_labels = __deserialize_training_data(training_data)

  def update_training_set(self, training_data):
    self.training_data, self.training_labels = __deserialize_training_data(training_data)

  def __deserialize_training_data(self, data):
    parsed_json = json.loads(data)
    training_data = [ parsed_entry['data'].split(",") for parsed_entry in parsed_json]
    training_labels = [ parsed_entry['result'] for parsed_entry in parsed_json]
    return [training_data, training_labels]
