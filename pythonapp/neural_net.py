import tensorflow as tf
import json

class NeuralNet:
  def __init__(self, training_data):
    self.update_training_set(training_data)

  def update_training_set(self, training_data):
    self.training_data, self.training_labels = self.__deserialize_training_data(training_data)
    self.batch_size = len(self.training_data)
    self.num_features = len(self.training_data[0])
    self.num_possibilities = len(self.training_labels[0])

  def __deserialize_training_data(self, data):
    parsed_json = json.loads(data)

    training_data_str = [ str(parsed_entry['data']).split(",") for parsed_entry in parsed_json]
    training_data = [ [ float(j) for j in i ] for i in training_data_str ]

    training_labels_str = [ str(parsed_entry['result']) for parsed_entry in parsed_json]
    training_labels = [ [1., 0.] if int(i) == 0 else [0., 1.] for i in training_labels_str ]

    return [training_data, training_labels]

  def set_model(self):
    self.input_layer = tf.placeholder(tf.float32, shape=[None, self.num_features])
    dense1_layer = tf.layers.dense(inputs=self.input_layer, units=self.num_features, activation=tf.nn.relu)
    dense2_layer = tf.layers.dense(inputs=dense1_layer, units=self.num_features / 2, activation=tf.nn.relu)
    output_layer = tf.layers.dense(inputs=dense2_layer, units=self.num_possibilities)
    self.model = output_layer

  def train(self):
    self.set_model()

    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(
                      logits=self.model,
                      labels=self.training_labels
                    )

    cost = tf.reduce_mean(cross_entropy)
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(cost)

    init = tf.global_variables_initializer()
    sess = tf.InteractiveSession()

    sess.run(init)
    for _ in range(200):
      _, c = sess.run([optimizer, cost], { self.input_layer: self.training_data })

    print("Finish!")
    print c
