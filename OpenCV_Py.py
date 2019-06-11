# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

pass  # ---------读取、显示、保存图像-----------
# Load an color image in grascale
# img = cv2.imread('dingdang.jpg', 1)  # 0 灰度图，1 彩色图
# # cv2.imshow('image', img)
# b, g, r = cv2.split(img)
# img2 = cv2.merge([r, g, b])
# plt.subplot(121)   # 1行2列 画在图的第1个位置
# plt.xticks([]), plt.yticks([])  # 隐藏 x/y轴标签
# plt.imshow(img)
# plt.subplot(122)  # 1行2列 画在图的第2个位置
# plt.imshow(img2)
# plt.xticks([]), plt.yticks([])
# plt.show()
#
# print("Enter 'ESC' for quit, 's' for save: \n")
# k = cv2.waitKey(000) & 0xff  # 等待时间 ms 0 为一直等待
#
# if k == 27:  # ESC 27
#     cv2.destroyAllWindows()
# elif k == ord('s'):  # wait for 's' key to save and exit
#     cv2.imwrite('copy.jpg', img)
#     cv2.destroyAllWindows()
# else:
#     print('You just entered key:', k)
# ---------- 保存图像---------
# cv2.namedWindow('image2', cv2.WINDOW_NORMAL)  # cv2.WINDOW_NORMAL 可自动调节图像大小
# img2 = cv2.imread('dingdang.jpg', 0)
# cv2.imshow('image2', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 保存图像
# cv2.imwrite('gray_dingdang.jpg', img2)
pass  # ---------绘图------------------
#
# # create a black image
# img = np.zeros((512, 512, 3), np.uint8)
#
# # Draw a diagonal blue line with thickness of 5px
# cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# cv2.imshow('line', img)
#
# # Draw a green rectangle with thickness of 3px
# cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# cv2.imshow('rectangle', img)
#
# # Draw a red circle with solid one
# cv2.circle(img, (447, 63), 63, (0, 0, 255), thickness=-1)   # -1 表示实心， thickness= 可省略，位置变量
# cv2.imshow('circle', img)
#
# # Draw a ellipse
# cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 270, (255, 0, 255), -1)
# cv2.imshow('ellipse', img)
#
# # Draw a pink polygon with thickness of 2px
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))  # -1 根据pts计算长度，rows*1*2
# cv2.polylines(img, [pts], True, (255, 0, 255), 2)  # True 闭合图形， False 未闭合图形
# cv2.imshow('polygon', img)
#
# # Add txt to image
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, "Nice to meet you!", (90, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
# # cv2.namedWindow('are you kidding me ')  # just creat a window
# cv2.imshow('Hello', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------鼠标当画笔-------------
# events = [i for i in dir(cv2) if 'EVENT' in i]  # 查看支持事件
# events = np.matrix(events)  # 转成矩阵方便查看
# print(events)
# # cv2_EVENT_FLAG_LBUTTON           左键拖拽
# # cv2_EVENT_FLAG_RBUTTON           右键拖拽
# # cv2_EVENT_FLAG_MBUTTON           中间拖拽
# # CV_EVENT_MOUSEMOVE               滑动
# # CV_EVENT_LBUTTONDOWN             左键点击
# # CV_EVENT_RBUTTONDOWN             右键点击
# # CV_EVENT_MBUTTONDOWN             中间点击
# # CV_EVENT_LBUTTONUP               左键释放
# # CV_EVENT_RBUTTONUP               右键释放
# # CV_EVENT_MBUTTONUP               中间释放
# # CV_EVENT_LBUTTONDBLCLK           左键双击
# # CV_EVENT_RBUTTONDBLCLK           右键双击
# # CV_EVENT_MBUTTONDBLCLK           中间释放


# def draw_circle(event, x, y, flags, param):
#     """mouse callback function"""
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, (255, 0, 0), 3)
#
#
# # 创建图像与窗口并将窗口与回调函数绑定
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)                                   #？？？？？？？？？？？？？？？？？
#
# while 1:
#     cv2.imshow('image', img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# # cv2.imwrite(r'C:\Users\IA204053\Desktop\qq.jpg', img) # 保存图象
# cv2.destroyAllWindows()


# # # 高级应用
# #
# # 当鼠标按下时变为True
# darwing = False
# # 如果mode 为 true 时绘制矩形， 按下'm' 变成绘制曲线
# mode = True
# ix, iy = -1, -1
#
#
# # 创建回调函数
# def draw_circle(event, x, y, flags, param):
#     global ix, iy, drawing, mode
# # 当按下左键时返回起始位置坐标
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
# # 鼠标左键按下并移动鼠标时绘制图形。 event 查看移动， flag 查看是否按下
# #     elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
# #         if drawing == True:
# #             if mode == True:
# #                 cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
# #             else:
# #                 r = int(np.sqrt((x-ix)**2 + (y-iy)**2))
# #                 cv2.circle(img, (x, y), r, (0, 255, 0), 1)
# # 松开鼠标，停止绘图 画图第一个参考点为按下时坐标，第二个参考点为鼠标松开时坐标
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         ix2, iy2 = x, y
#         if mode == True:
#             # cv2.rectangle(img, (ix, iy), (ix2, iy2), (0, 255, 0), 1)
#             cv2.rectangle(img, (ix, iy), (ix2, iy2), (b, g, r), 1)
#         else:
#             rid = int(np.sqrt((ix2 - ix) ** 2 + (iy2 - iy) ** 2)/2)
#             # cv2.circle(img, (int((ix2+ix)/2), int((iy2+iy)/2)), rid, (0, 255, 0), 1)
#             cv2.circle(img, (int((ix2 + ix) / 2), int((iy2 + iy) / 2)), rid, (b, g, r), 1)
#
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
# # while 1:
# #     cv2.imshow('image', img)
# #     k = cv2.waitKey(1)
# #     if k == ord('m'):
# #         mode = not mode
# #     elif k == 27:
# #         break
pass  # ---------使用滑动条-------------
#
#
# def nothing(x):
#     pass
#
#
# # # 创建一幅黑色图像
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
#
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
#
# switch = '0:OFF\n1:ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)
# while 1:
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode    # 结合画矩形画圆程序，可调节画笔颜色
#     elif k == 27:
#         break
#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     s = cv2.getTrackbarPos(switch, 'image')
#
#     if s == 0:
#         img[0: 50, 0: 50] = 0
#     else:
#         img[0: 50, 0: 50] = [b, g, r]
#
# cv2.destroyAllWindows()
pass  # ---------给图像扩充边-----------
# BLUE = [0, 0, 255]
# img1 = cv2.imread('th.jpg')
# r, g, b = cv2.split(img1)
# img1 = cv2.merge([b, g, r])
# W = int((img1.shape[0]))
# print(W, img1.shape)
# L = int(img1.shape[1])
# replicate = cv2.copyMakeBorder(img1, W, W, L, L, cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img1, W, W, L, L, cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img1, 200, 200, 200, 200, cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img1,  100, 100, 100, 100, cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img1, 200, 200, 200, 200, cv2.BORDER_CONSTANT, value=BLUE)
# plt.subplot(231), plt.imshow(img1), plt.title('ORIGINAL')
# plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
# plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
# plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
# plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
# plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
# plt.xticks([]), plt.yticks([])
# plt.show()

# mm = np.zeros(img1.shape，uint8)
# cv2.namedWindow('mm')
# cv2.imshow('mm', reflect)
# cv2.imshow('mm1', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------图像加法---------------
# img1 = cv2.imread('th.jpg')
# img2 = cv2.imread('dingdang.jpg')
# img3 = img2 + img1
# img4 = cv2.add(img2, img1)
# dst = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
# plt.subplot(221)
# plt.imshow(img1)
# plt.subplot(222)
# plt.imshow(img3)
# plt.subplot(223)
# plt.imshow(img4)
# plt.subplot(224)
# plt.imshow(dst)a
# plt.show()
# # 图像平滑切换
# a = 0
# while (a <= 1):
#    dst2 = cv2.addWeighted(img1, 1-a, img2, a, 0)
#    a = a + 0.01
#    cv2.waitKey(50)
#    cv2.imshow('dst2', dst2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------按位运算, 掩模运算------
# # 加载图像
# img1 = cv2.imread('tt.jpg', 1)
# img2 = cv2.imread('lf.jpg', 1)
# # cv2读取的是像素是bgr, plt 是 rgb,通过split 与 merge进行调整
# b1, g1, r1 = cv2.split(img1)
# b2, g2, r2 = cv2.split(img2)
# img1 = cv2.merge([r1, g1, b1])
# img2 = cv2.merge([r2, g2, b2])
# # 把叮当猫放到图片左上角，先创建ROI
# rows1, cols1, channels1 = img1.shape
# rows2, cols2, channels2 = img2.shape
# roi = img1[rows1-rows2:rows1, 0:cols2]
#
# # 创建叮当猫的掩模及其反向掩模
# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# # mask 中将灰度175~255之间的值取为1，小于175的取0 （mask_inv 为图像轮廓及颜色较深的内容区域）
# ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)   # cv2.bitwise_not 位取反操作
# # 取roi中与mask 中不为零的值对应的相素值，其他值为0，mask中内容部分为0
# img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
# # 取roi中与mask_inv 中不为零的值对应的相素值，其他值为0，mask_inv中内容部分为1
# img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
#
# dst = cv2.add(img1_bg, img2_fg)
# img1[rows1-rows2:rows1, 0:cols2] = dst
#
# plt.subplot(231)
# plt.title('mask')
# plt.imshow(mask)
# plt.subplot(232)
# plt.imshow(img2)
# plt.subplot(233)
# plt.title('img1_bg')
# plt.imshow(img1_bg)
# plt.subplot(234)
# plt.title('img2_fg')
# plt.imshow(img2_fg)
# plt.subplot(235)
# plt.imshow(img2gray)
# plt.subplot(236)
# plt.imshow(img1)
# plt.show()
# print(mask[1, 1], img2gray[1, 1])
pass  # ---------颜色空间转换-----------
# # cv2.cvtColor(input_image， flag)
# # BGR to Gray  flag = cv2.COLOR_BGR2GRAY
# # BGR to HSV   flag = cv2.COLOR_BGR2HSV  注：OpenCV中取值范围 H[0,179], S[0,255], V[0,255]
# img = cv2.imread('dingdang.jpg', 1)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # 设定红色的阈值
# lower_red1 = np.array([00, 50, 50])
# upper_red1 = np.array([10, 255, 255])
# lower_red2 = np.array([156, 50, 50])
# upper_red2 = np.array([179, 255, 255])
# # 根据阈值创建掩膜，注意，红色的H值分布范围为H [0,10]U[156,180] S[43,255] V[43,255]
# mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
# mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
# mask = cv2.add(mask1, mask2)
# mask_inv = cv2.bitwise_not(mask)
# dst = cv2.bitwise_and(img, img, mask=mask_inv)
# img2 = np.zeros(img.shape, np.uint8)
# img2[:, :] = [0, 255, 0]
# bg = cv2.bitwise_and(img2, img2, mask=mask)
# img_g = cv2.add(bg, dst)
# cv2.imshow('orig', img)
# cv2.imshow('mask_inv', mask_inv)
# cv2.imshow('img_g', img_g)
# cv2.imshow('mask', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # BGR 与 HSV值映射关系
# # 这里的三层括号应该分别对应于 cvArray，cvMat，IplImage
# green = np.uint8([[[0, 250, 0]]])
# green_HSV = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# print(green_HSV)
pass  # ---------图像缩放-----------


