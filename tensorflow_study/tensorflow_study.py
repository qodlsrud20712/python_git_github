import tensorflow as tf
import matplotlib.pyplot as plt

# class Model():
#     def __init__(self):
#         self.W = tf.Variable(5.0)
#         self.b = tf.Variable(0.0)
#
#
#     def __call__(self, x):
#         return self.W *x + self.b
#
# model = Model()
#
# assert model(3.0).numpy() == 15.0
#
# def loss(predicted_y, desired_y):
#     return tf.reduce_mean(tf.square(predicted_y - desired_y))
#
# TRUE_W = 3.0
# TRUE_b = 2.0
#
# NUM_EXAMPLES = 1000
#
# inputs = tf.random.normal(shape=[NUM_EXAMPLES])
# noise = tf.random.normal(shape=[NUM_EXAMPLES])
# outputs = inputs * TRUE_W+TRUE_b +noise
#
# plt.scatter(inputs, outputs, c='b')
# plt.scatter(inputs, model(inputs), c='r')
# plt.show()
#
# print('현재 손실: '),
# print(loss(model(inputs), outputs).numpy())
#
# def train(model, inputs, outputs, learning_rate):
#   with tf.GradientTape() as t:
#     current_loss = loss(model(inputs), outputs)
#   dW, db = t.gradient(current_loss, [model.W, model.b])
#   model.W.assign_sub(learning_rate * dW)
#   model.b.assign_sub(learning_rate * db)
#
#
# Ws, bs = [], []
# epochs = range(10)
# for epoch in epochs:
#   Ws.append(model.W.numpy())
#   bs.append(model.b.numpy())
#   current_loss = loss(model(inputs), outputs)
#
#   train(model, inputs, outputs, learning_rate=0.1)
#   print('에포크 %2d: W=%1.2f b=%1.2f, 손실=%2.5f' %
#         (epoch, Ws[-1], bs[-1], current_loss))
#
# # 저장된 값들을 도식화합니다.
# plt.plot(epochs, Ws, 'r',
#          epochs, bs, 'b')
# plt.plot([TRUE_W] * len(epochs), 'r--',
#          [TRUE_b] * len(epochs), 'b--')
# plt.legend(['W', 'b', 'true W', 'true_b'])
# plt.show()


