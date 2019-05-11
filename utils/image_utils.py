import tensorflow as tf


class ImageReader:

  def __init__(self):
    # image reading graph
    self.tf_graph = tf.Graph()
    with self.tf_graph.as_default():
      self.tf_image_path = tf.placeholder(tf.string, [])
      
      tf_image = tf.read_file(self.tf_image_path)
      tf_image = tf.image.decode_image(tf_image, channels=3, dtype=tf.uint8)
      
      self.tf_image = tf_image

      init = tf.global_variables_initializer()
      self.tf_session = tf.Session(config=tf.ConfigProto(
          device_count={'GPU': 0}
      ))
      self.tf_session.run(init)
  
  def read(self, image_path):
    image = self.tf_session.run(self.tf_image, feed_dict={self.tf_image_path:image_path})
    return image


class ImageWriter:

  def __init__(self):
    # image writing graph
    self.tf_graph = tf.Graph()
    with self.tf_graph.as_default():
      self.tf_image = tf.placeholder(tf.uint8, [None, None, 3])
      self.tf_image_path = tf.placeholder(tf.string, [])

      tf_image = tf.image.encode_png(self.tf_image)
      tf_write_op = tf.write_file(self.tf_image_path, tf_image)

      self.tf_write_op = tf_write_op

      init = tf.global_variables_initializer()
      self.tf_session = tf.Session(config=tf.ConfigProto(
          device_count={'GPU': 0}
      ))
      self.tf_session.run(init)
  
  def write(self, image, image_path):
    self.tf_session.run(self.tf_write_op, feed_dict={self.tf_image:image, self.tf_image_path:image_path})

