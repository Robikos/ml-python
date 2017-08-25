import tensorflow as tf
import json

class NeuralNet:
  def __init__(self, training_data):
    self.training_data, self.training_labels = self.__deserialize_training_data(training_data)

  def update_training_set(self, training_data):
    self.training_data, self.training_labels = self.__deserialize_training_data(training_data)

  def __deserialize_training_data(self, data):
    parsed_json = json.loads(data)

    training_data_str = [ str(parsed_entry['data']).split(",") for parsed_entry in parsed_json]
    training_data = [ [ int(j) for j in i ] for i in training_data_str ]

    training_labels_str = [ str(parsed_entry['result']) for parsed_entry in parsed_json]
    training_labels = [ int(i) for i in training_labels_str ]

    return [training_data, training_labels]

  def model(self):
    data_dimention = len(self.training_data[0])
    input_layer = tf.placeholder(tf.int32, shape=(data_dimention))
    dense1_layer = tf.layers.dense(inputs=input_layer, units=data_dimention, activation=tf.nn.relu)
    dense2_layer = tf.layers.dense(inputs=dense1_layer, units=data_dimention / 2, activation=tf.nn.relu)
    output_layer = tf.layers.dense(inputs=dense2_layer, units=1)
    output_layer

  def train(self):
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=self.model(), labels=self.training_labels)
    cost = tf.reduce_mean(cross_entropy)
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(cost)

    init = tf.global_variables_initializer()
    sess = tf.Session()

    sess.run(init)
    for _ in range(20):
      _, c = sess.run([optimizer, cost], { input_layer: self.training_data })

    print("Finish!")
    print c
