import tensorflow as tf
from pprint import pformat


class MyDenseLayer(tf.keras.layers.Layer):

  def __init__(self, input_dim, out_dim):
    super(MyDenseLayer, self).__init__()

    self.W = self.add_weight(name='W', shape=[input_dim, out_dim])
    self.b = self.add_weight(name='b', shape=[1, out_dim])

    print(pformat(vars((self))))

  def call(self, inputs):

    z = tf.matmul(inputs, self.W) + self.b

    output = tf.math.sigmoid(z)

    return output


if __name__ == '__main__':
  layer = MyDenseLayer(4, 2)