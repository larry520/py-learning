# -*- encoding: utf-8 -*-

import input_data
import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# MNIST python 自带教程中有minst下载链接 及配置文件
# from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# placeholder 占位符  [None, 784] None 表示可为任意行, 784列的二维矩阵
x = tf.placeholder("float", [None, 784])

# W, b 是需要被训练的值，其初始值可以为任意设置
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 建立训练模型
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 新占位符用于输入正确值
y_ = tf.placeholder("float", [None, 10])

# 计算交叉熵
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# 采用梯度下降法，0.01的学习速率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 创建一个操作初始化创建的变量
init = tf.global_variables_initializer()
#  启动模型并初化化变量
# sess = tf.Session()
#
# # 交互式环境
sess = tf.InteractiveSession()
sess.run(init)

for i in range(1000):
    # batch_xs, batch_ys = mnist.train.next_batch(100)
    # sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # sess = tf.InteractiveSession() 交互式不需要 see.run(fetches, feed_dict...)
    # 可直接使用 fetches.sess(feed_dict...)
    batch = mnist.train.next_batch(50)
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})

correct_prediction = tf.equal(tf.math.argmax(y, 1), tf.math.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
