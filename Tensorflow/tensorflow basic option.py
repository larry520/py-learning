# -*- encoding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

pass  # -------------------TensorFlow 示例--------------2019-8-1 14:25:43
# # 使用numpy 生成假数据
# x_data = np.float32(np.random.rand(2, 100))
# y_data = np.dot([0.100, 0.200], x_data) + 0.300
#
# # 构造一个线性模型
# b = tf.Variable(tf.zeros([1]))
# w = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
# y = tf.matmul(w, x_data) + b
#
# # 最小化方差
# loss = tf.reduce_mean(tf.square(y - y_data))
# optimizer = tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)
#
# # 初始化变量
# init = tf.global_variables_initializer()
#
# # 启动图（graph)
# sess = tf.Session()
# sess.run(init)
#
# # 拟合平面
# for step in range(0, 201):
#     sess.run(train)
#     if step % 20 == 0:
#         print(step, sess.run(w), sess.run(b))
pass  # -------------------tf.keras--------------2019-8-2 14:25:43
import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=2)
model.evaluate(x_test, y_test)





