# -*- encoding: utf-8 -*-

import input_data
# MNIST python 自带教程中有minst下载链接 及配置文件
# from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)


