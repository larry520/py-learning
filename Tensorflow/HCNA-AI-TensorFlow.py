# -*- coding: utf-8 -*-
# tensorBoard --logdir E:\GitHub_repo\py-learning\OpenCv\log\mnist_with_summaries --host=localhost
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# hello = tf.constant('Hello, TensorFlow!')
# # sess = tf.Session()
# with tf.Session() as sess:
#     print(sess.run(hello))
#     print(hello.eval())
# sess.close()
# a = tf.constant(3)
# b = tf.constant(4)
#
# with tf.Session() as sess:   # 与python中with用法一致，当程序结束后自动关闭Session
#     print("相加： %i" % sessF.run(a+b))
#     print("相乘： %i" % sess.run(a*b))
pass  # # -----------TensorFlow 默认会话---------------------------------
# sess = tf.InteractiveSession()
# # 建立两个矩阵变量w1 和 w2
# # tf.random_normal(shape,
# #                   mean=0.0,
# #                   stddev=1.0,
# #                   dtype=dtypes.float32,
# #                   seed=None,
# #                   name=None)
# # 产生随机正态分布
# # shape 表示矩阵的维度，例如：
# # tf.random_normal([2,3],mean=1.0, stddev=1.0)是一个 2 行 3 列的矩阵，
# # mean 表示均值，默认为 0.0，stddev 表示标准差，默认为 1.0
# # seed 表示随机数种子，默认为 None
# w1 = tf.Variable(tf.random_normal([2, 3], mean=1.0, stddev=1.0))
# w2 = tf.Variable(tf.random_normal([3, 1], mean=1.0, stddev=1.0))
# # 定义常量矩阵，注意： 这里不是一维数组
# x = tf.constant([[0.7, 0.9]])
# # 初始化全局变量，这里由于只有 w1 和 w2 没有被初始化（之前只是定义了 w1 和 w2 的 tensor，并没有被
# # 初始化），故这一步只会初始化 w1 和 w2.
# tf.global_variables_initializer().run()
# # 计算矩阵相乘a = x*w1
# a = tf.matmul(x, w1)
# b = tf.matmul(a, w2)
# print(b.eval())
pass  # -------------TensorFlow tf.Variable 变量的定义-------------------
# tf.reset_default_graph()  # 重置计算图
# # 定义 get_variable变量
# # 变量如果遇到同名的会重命名varname，varname_1,... varname_n
# var1 = tf.Variable(10.0, name="varname")
# var2 = tf.Variable(11.0, name="varname")
# # 变量默认命名为 Varname
# var3 = tf.Variable(12.0)
# var4 = tf.Variable(13.0)
# var41 = tf.Variable(13.0)
# # get_variable变量
# # tf.variable_scope 变量管理器
# with tf.variable_scope("test1"):
#     var5 = tf.get_variable("varname", shape=[2], dtype=tf.float32)
#     var51 = tf.Variable(1.0, name="varname")
#
# with tf.variable_scope("test2"):
#     var6 = tf.get_variable("varname", shape=[2], dtype=tf.float32)
#
# print("var1:", var1.name)
# print("var2:", var2.name)
# print("var3:", var3.name)
# print("var4:", var4.name)
# print("var5:", var5.name)
# print("var6:", var51.name)
pass  # # -----------TensorBoard 可视化----------------------------------
# plotdata = {"batchsize": [], "loss": []}
#
#
# def moving_average(a, w=10):
#     if len(a) < w:
#         return a[:]
#     return [val if idx < w else sum(a[(idx - w): idx])/w for idx, val in enumerate(a)]
#
#
# # 生成模拟数据
# train_X = np.linspace(-1, 1, 100)
# train_Y = 2*train_X + np.random.randn(*train_X.shape)*0.3  # y=2x，但是加入了噪声
# # 重置计算图
# plt.plot(train_X, train_Y, 'ro', label='Original data')
# plt.legend()  # 增加图例,将label内容显示到图中
# plt.show()
#
# tf.reset_default_graph()
#
# # 创建模型
# X = tf.placeholder("float")
# Y = tf.placeholder("float")
# # 模型参数
# W = tf.Variable(tf.random_normal([1]), name="weight")
# b = tf.Variable(tf.zeros([1]), name="bias")
#
# # 前向结构
# z = tf.multiply(X, W)+b
# tf.summary.histogram('z', z)  # 将预测值以直方图显示
#
# # 反向优化
# cost = tf.reduce_mean(tf.square(Y-z))
# tf.summary.scalar('loss_function', cost)
# learning_rate = 0.01
# # Gradient descent  梯度下降
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
#
# # 初始化变量
# init = tf.global_variables_initializer()
#
# # 参数设置
# training_epochs = 20
# display_step = 2
#
# # 启动Session
# with tf.Session() as sess:
#     sess.run(init)
#     # 合并所有summary
#     merged_summary_op = tf.summary.merge_all()
#     # 创建 summary_writer, 用于写文件
#     summary_writer = tf.summary.FileWriter('log/mnist_with_summaries', sess.graph)
#
#     # 向模型中写入数据
#     for epoch in range(training_epochs):
#         for(x, y) in zip(train_X, train_Y):
#             sess.run(optimizer, feed_dict={X: x, Y: y})
#
#             # 生成summary
#             summart_str = sess.run(merged_summary_op, feed_dict={X: x, Y: y})
#             summary_writer.add_summary(summart_str, epoch)  # 将summary写入文件
#         # 显示训练中的详细信息
#         if epoch % display_step ==0:
#             loss = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
#             print("Epoch:", epoch+1, "cost=", loss, "W=", sess.run(W), "b=", sess.run(b))
#             if not(loss ==  "NA"):
#                 plotdata["batchsize"].append(epoch)
#                 plotdata["loss"].append(loss)
#     print("Finished!")
#     print("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}),
#           "W=", sess.run(W), "b=", sess.run(b))
#     print("cost=", cost.eval({X: train_X, Y: train_Y}))
#
#     # 结果可视化
#     plt.plot(train_X, train_Y, 'ro', label="Original data")
#     plt.plot(train_X, sess.run(W)*train_X + sess.run(b), label="Fitted line")
#     plt.legend()
#     plt.show()
#
#     plotdata["avgloss"] = moving_average(plotdata["loss"])
#     plt.figure(1)
#     plt.subplot(211)
#     plt.plot(plotdata["batchsize"], plotdata["avgloss"], 'b--')
#     plt.xlabel('Minibatch number')
#     plt.ylabel('Loss')
#     plt.title('Minibatch run vs. Training loss')
#     plt.show()
#
#     # 模型结果测试
#     print("x=0.2, z=", sess.run(z, feed_dict={X: 0.2}))
pass  # -------------数据读取与处理----------------2019-7-29 22:11:15
# filename_queue = tf.train.string_input_producer(["tf_read.csv"])  # 读取已有数据
# # filename_queue = tf.data.Dataset.from_tensor_slices("tf_read.csv")
# reader = tf.data.TextLineDataset("tf_read.csv")
# # 获取队列值
# key, value = reader.read(filename_queue)
# # key 返回的是读取文件和行数信息
# # value 是按行读取到的原始字符串，送到下面的 decoder 去解析
# # key 是文件信息和当前读取的行数，value 是原始字符串。
# record_defaults = [[1.], [1.], [1.], [1.]]   # 这里的数据类型决定了读取的数据类型，
# # 而且必须是 list 形式
# # 解析出的每一个属性都是 rank 为 0 的标量
# col1, col2, col3, col4 = tf.decode_csv(value, record_defaults=record_defaults)
# features = tf.stack([col1, col2, col3])
#
# # 初始化
# init_op = tf.global_variables_initializer()
# local_init_op = tf.local_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init_op)
#     sess.run(local_init_op)
#
#     # start population the filename queue 开启一个协调器
#     coord = tf.train.Coordinator()
#     # 使用start_queue_runners 进行队列填充
#     threads = tf.train.start_queue_runners(coord=coord)
#
#     try:
#         for i in range(30):
#             example, label = sess.run([features, col4])
#             print(example)
#             print(label)
#     except tf.errors.OutOfRangeError:
#         print('Done!')
#     finally:   # 执行完后协调器coord发出所有线程终止信号
#         coord.request_stop()
#         print("all threads are asked to stop!")
#         coord.join(threads)  # 把线程加入主线程，等待threads结束
#         print('all threads are stooped!')


