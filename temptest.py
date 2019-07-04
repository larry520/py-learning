import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import tensorflow as tf
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(3)
b = tf.constant(4)
with tf.Session()  as sess:
    print("相乘： %i" % sess.run(a*b))


plotdata = { "batchsize":[], "loss":[] }
def moving_average(a, w=10):
    if len(a) < w:
        return a[:]
    return [val if idx < w else sum(a[(idx-w):idx])/w for idx, val in
            enumerate(a)]

#生成模拟数据
train_X = np.linspace(-1, 1, 100)
train_Y = 2*train_X + np.random.randn(*train_X.shape)*0.3    # y=2x，但是加入了噪声
#图形显示
# plt.plot(train_X, train_Y, 'ro', label='Original data')
# plt.legend()
plt.show()
tf.reset_default_graph()