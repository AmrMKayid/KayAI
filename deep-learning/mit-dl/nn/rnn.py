import tensorflow as tf
from pprint import pformat


class MyRNNLayer(tf.keras.layers.Layer):

  def __init__(self, rnn_units, input_dim, output_dim):
    super(MyRNNLayer, self).__init__()

    # Initializa weight metrices
    self.W_xh = self.add_weight(name='w_xh', shape=[rnn_units, input_dim])
    self.W_hh = self.add_weight(name='w_hh', shape=[rnn_units, rnn_units])
    self.W_hy = self.add_weight(name='w_hy', shape=[output_dim, rnn_units])

    # Initialize hidden state to zeros
    self.h = tf.zeros([rnn_units, 1])

    print(pformat(vars((self))))

  def call(self, inputs):

    # Update the hidden state
    self.h = tf.math.tanh(self.W_hh * self.h * self.W_xh * inputs)

    # compute the output
    output = self.W_hy * self.h

    return output, self.h


if __name__ == '__main__':
  layer = MyRNNLayer(8, 4, 2)