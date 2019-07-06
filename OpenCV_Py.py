# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
from PIL import Image
import time

def nothing(x):
    pass


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


# # 高级应用
#
# 当鼠标按下时变为True
# darwing = False
# # 如果mode 为 true 时绘制矩形， 按下'm' 变成绘制曲线
# mode = True
# ix, iy = -1, -1
# #
#
# # 创建回调函数
# def draw_circle(event, x, y, flags, param):
#     global ix, iy, drawing, mode
# # 当按下左键时返回起始位置坐标
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
# # 鼠标左键按下并移动鼠标时绘制图形。 event 查看移动， flag 查看是否按下
#     elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
#             else:
#                 r = int(np.sqrt((x-ix)**2 + (y-iy)**2))
#                 cv2.circle(img, (x, y), r, (0, 255, 0), 1)
# # 松开鼠标，停止绘图 画图第一个参考点为按下时坐标，第二个参考点为鼠标松开时坐标
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         ix2, iy2 = x, y
#         if mode == True:
#             cv2.rectangle(img, (ix, iy), (ix2, iy2), (0, 255, 0), 1)
#             # cv2.rectangle(img, (ix, iy), (ix2, iy2), (b, g, r), 1)
#         else:
#             rid = int(np.sqrt((ix2 - ix) ** 2 + (iy2 - iy) ** 2)/2)
#             # cv2.circle(img, (int((ix2+ix)/2), int((iy2+iy)/2)), rid, (0, 255, 0), 1)
#             cv2.circle(img, (int((ix2 + ix) / 2), int((iy2 + iy) / 2)), rid, (b, g, r), 1)
#
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
# while 1:
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1)
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
pass  # ---------使用滑动条-------------
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
pass  # ---------图像加法/图像拼接---------------
# np.hstack([img1, img2])
# np.vstack([img1, img2])

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
# cv2.cvtColor(input_image， flag)
# BGR to Gray  flag = cv2.COLOR_BGR2GRAY
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
pass  # ---------图像缩放--------------
# # 缩放函数 cv2.resize()
# # 缩放图像尺寸可自定义也可以指定缩放因子
# # 缩放时的插值方法：cv2.INTER_AREA(可避免条纹), 扩展用 cv2.INTER_CUBIC 或 cv2.INTER_LINEAR，后者速度更快
# img = cv2.imread('dingdang.jpg', 1)
# # cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)
# res1 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# height, width = img.shape[:2]  # 切片，img.shape = [height/row, width/cols, channel]
# res2 = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_LINEAR)
# cv2.imshow('res1', res1)
# cv2.imshow('res2', res2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------图像平移--------------
# img = cv2.imread('dingdang.jpg', 1)
# rows, cols = img.shape[:2]
# # 创建平移矩阵
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# # 第三个参数为输出图像的大小，格式为（宽，高）
# dst = cv2.warpAffine(img, M, (cols, rows))
# cv2.imshow('img', img)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------图像旋转--------------
# img = cv2.imread('dingdang.jpg', 1)
# rows, cols = img.shape[:2]
# MR = np.float32([[1, 0, int(cols/2)], [0, 1, int(rows/2)]])
# dst = cv2.warpAffine(img, MR, (2 * cols, 2 * rows))
# # 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# # 可以通过设置旋转中心，缩放因子，以及窗口大小(图片缩放比例)来防止旋转后超出边界的问题
# M = cv2.getRotationMatrix2D((cols, rows), 45, 0.5)
# # 第三个参数是输出图像的尺寸
# dst1 = cv2.warpAffine(dst, M, (2 * cols, 2 * rows))
# while 1:
#     cv2.imshow('dst', dst)
#     cv2.imshow('dst1', dst1)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()
pass  # ---------仿射变换/平面变换------
# img = cv2.imread('dingdang.jpg', 1)
# rows, cols = img.shape[:2]
# # 根据input 与 output 图像上3个点对应关系，确定映射矩阵
# pts1 = np.float32([[0, 0], [0, 2], [2, 0]])
# pts2 = np.float32([[0, 0], [2, 3], [3, -2]])
# # 得到变换矩阵，图像的变换主要取决于变换矩阵M
# M = cv2.getAffineTransform(pts1, pts2)
# # 进行变换
# dst = cv2.warpAffine(img, M, (2*cols, 2*rows))
# cv2.imshow('orig', img)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------透视变换/立体变换------      2019-6-11 21:37:49
# img = cv2.imread('dingdang.jpg', 1)
# rows, cols = img.shape[:2]
# M2 = np.float32([[1, 0, 0], [0, 1, rows/2]])
# img_m = cv2.warpAffine(img, M2, (2 * cols, 2 * rows))
# # 根据input 与 output 图像上3个点对应关系，确定映射矩阵
# pts1 = np.float32([[0, 0], [0, 2], [2, 0], [2, 2]])
# pts2 = np.float32([[0, 0], [1, 3], [-3, 1], [-1.95, 4.03]])
# # 得到变换矩阵，图像的变换主要取决于变换矩阵M
# M = cv2.getPerspectiveTransform(pts1, pts2)
# # 进行变换
# dst = cv2.warpPerspective(img_m, M, (2 * cols, 2 * rows))
# # 将图像向中间移动
#
# cv2.imshow('orig', img)
# cv2.imshow('img_m', img_m)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)&0xFF
# cv2.destroyAllWindows()
pass  # ---------图像简单阈值-----------------   2019-6-12 8:34:41
# # cv2.threshold(src, thresh, maxval, type, dst=None) 阀值处理函数
# img = cv2.imread('dingdang.jpg', 0)  # 阀值处理图片需是灰度图
# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # pix>thresh => 255 else 0
# ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # pix<thresh => 255 else 0
# ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # pix<thresh => 0
# ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # pix>thresh => 0
# ret, thresh5 = cv2.threshold(img, 80, 255, cv2.THRESH_TRUNC)  # pix>thresh => thresh
# plt.figure(num='Dingdang', figsize=(10, 10))
# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2, 3, i+1)
#     plt.title(titles[i])
#     plt.imshow(images[i], cmap='gray')
#     plt.axis('off')
#
# plt.show()
# cv2.imshow('trunc', thresh5)  # 当整体图片灰度较低时,plt.imshow()显示异常
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------自适应阈值-----------------  2019-6-12 14:24:29
# 对于打光原因导致的亮度不均可有较明显的改善
# img = cv2.imread('jgg.jpg', 0)
# # 中值滤波, 减小图像中的噪点
# img = cv2.medianBlur(img, 5)
# ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# # 11 为 Block size, 2 为 C 值
# th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                             cv2.THRESH_BINARY, 11, 2)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                             cv2.THRESH_BINARY, 11, 2)
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#           'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in range(4):
#     plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.axis('off')
# # plt.subplot(121)
# # plt.imshow(images[3], 'gray')
# # plt.axis('off')
# # plt.subplot(122)
# # imga = cv2.medianBlur(images[3], 5)
# # plt.imshow(imga, 'gray')
# # plt.axis('off')
# plt.show()
pass  # ---------Otsu’s 二值化-----------------  2019-6-12 14:51:8
# # 主要针对直方图有两个波峰的情形,意味着图片灰度主要集中在两个区域
# # img = cv2.imread('jgg.jpg', 0)
# img = cv2.imread('ostu.jpg', 0)
# # global thresholding
# ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#
# # Otsu's thresholding
# ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
# # Otsu's thresholding after Gaussian filtering
# # (5,5) 为高斯核大小, 0 为标准差
# blur = cv2.GaussianBlur(img, (5, 5), 0)
# ret3, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
#
# # plot all the images and their histograms
# images = [img, 0, th1,
#           img, 0, th2,
#           blur, 0, th3]
# titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
#           'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
#           'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
# for i in range(3):
#     plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
#     plt.title(titles[i*3]), plt.axis('off')
#     plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
#     plt.title(titles[i*3+1]), plt.axis('off')
#     plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
#     plt.title(titles[i*3+2]), plt.axis('off')
# plt.show()
# # 加中值滤波减小噪点
# cv2.imshow('global', th1)
# th1 = cv2.medianBlur(th1, 5)
# th1 = cv2.medianBlur(th1, 5)
# cv2.imshow('global_medi', th1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------图像平滑-----------------   2019-6-12 16:2:12
# # 1.cv2.blur(img, (3, 3))  进行均值滤波
# # 参数说明：img表示输入的图片， (3, 3) 表示进行均值滤波的方框大小
# #
# # 2. cv2.boxfilter(img, -1, (3, 3), normalize=True) 表示进行方框滤波，
# # 参数说明当normalize=True时，与均值滤波结果相同， normalize=False，表示对加和后的结果不进行平均操作，大于255的使用255表示
# #
# # 3. cv2.Guassianblur(img, (3, 3), 0) 表示进行高斯滤波，
# # 参数说明: (x,y)高斯核的宽与高,计算与当前值得距离(必须为奇数), 0 为标准差
# #
# # 4. cv2.medianBlur(img, 3) #中值滤波，过滤椒盐噪声,保留边缘.相当于将9个值进行排序，取中值作为当前值
# # 参数说明：img表示当前的图片，3表示当前的方框尺寸
# #
# # 5. cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)  # 滤波保留边界
# # 参数说明:d 表示领域直径,两个75分别是空间高斯函数标准差,灰度值相似性高斯函数标准差
# #
# # 使用不同的低通滤波器对图像进行模糊
# # 使用自定义的滤波器对图像进行卷积（2D 卷积）
# img = cv2.imread('girl.jpg', 1)
#
# kernel = np.ones((5, 5), np.float32) / 36
# # cv.Filter2D(src, dst, kernel, anchor=(-1, -1))
# # ddepth –desired depth of the destination image;
# # if it is negative, it will be the same as src.depth();
# # the following combinations of src.depth() and ddepth are supported:
# # src.depth() = CV_8U, ddepth = -1/CV_16S/CV_32F/CV_64F
# # src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
# # src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F
# # src.depth() = CV_64F, ddepth = -1/CV_64F
# # when ddepth=-1, the output image will have the same depth as the source.
# # 自定义方框均值滤波
# dst = cv2.filter2D(img, -1, kernel)
# # 方框均值滤波
# dst = cv2.blur(img, (5, 5))
# # 中值滤波
# dst = cv2.medianBlur(img, 5)
# # 高斯模糊
# # dst = cv2.GaussianBlur(img, (5, 5), 0)
# # 双边滤波
# dst = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow('orig', img)
# cv2.imshow('st', dst)
# cv2.waitKey(0)
# # 自适应阀值分割
# dst2 = cv2.adaptiveThreshold(dst[:, :, 0], 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                              cv2.THRESH_BINARY, 11, 2)
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst2, cmap='gray'), plt.title('Averaging')
# plt.axis('off')
# plt.show()
pass  # ---------形态学转换-腐蚀/膨胀-----------------   2019-6-12 20:25:50  - 2019-6-12 21:13:43
# # 一种去噪声的方法, 腐蚀可以分开连接的物体,膨胀可以把未连接的物体连接
# img = cv2.imread('j.jpg', 0)
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(img, kernel, iterations=1)
# dilation = cv2.dilate(img, kernel, iterations=1)
# plt.subplot(131), plt.title('orig'), plt.imshow(img, cmap='gray')
# plt.subplot(132), plt.title('erosion'), plt.imshow(erosion, cmap='gray')
# plt.subplot(133), plt.title('dilation'), plt.imshow(dilation, cmap='gray')
# plt.show()
pass  # ---------为图像添加噪声-----------------   2019-6-13 10:51:16
#
#
# def sp_noise(image, prob):
#     """
#     :param image:  原始图像
#     :param prob: 噪声比例
#     :return: 添加椒盐噪声的图像
#     """
#     output = np.zeros(image.shape, np.uint8)
#     thres = 1 - prob
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = 0
#             elif rdn > thres:
#                 output[i][j] = 255
#             else:
#                 output[i][j] = image[i][j]
#     return output
#

# def gasuss_noise(image, mean=0, var=0.001):
#     """
#     :param image:  原始图像
#     :param mean:  均值
#     :param var:  方差
#     :return:  添加高斯噪声的图像
#     """
#     image = np.array(image / 255, dtype=float)
#     noise = np.random.normal(mean, var ** 0.5, image.shape)    # 高斯分布也叫正态分布
#     out = image + noise
#     if out.min() < 0:
#         low_clip = -1.
#     else:
#         low_clip = 0.
#     out = np.clip(out, low_clip, 1.0)
#     out = np.uint8(out * 255)
#     # cv.imshow("gasuss", out)
#     return out
#

pass  # ---------形态学转换-开运算/闭运算----------------- 2019-6-13 10:46:44
# # 先进性腐蚀再进行膨胀就叫做开运算, 反之为闭运算
# # opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # 开运算
# # closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # 闭运算
# # 开运算用于去除背景中的噪声
# # 闭运算用于去除前景中的噪声(黑点)
# img = cv2.imread('j.jpg', 0)
# img = gasuss_noise(img)
# # img = sp_noise(img, 0.01)
# kernel = np.ones((5, 5), np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# plt.subplot(131), plt.title('orig'), plt.imshow(img, cmap='gray')
# plt.subplot(132), plt.title('opening'), plt.imshow(opening, cmap='gray')
# plt.subplot(133), plt.title('closing'), plt.imshow(closing, cmap='gray')
# plt.show()
pass  # ---------形态学梯度/礼帽/黑帽--------   2019-6-13 14:54:33
# # 梯度：一幅图像膨胀与腐蚀的差，结果看上去就像前景物体的轮廓。
# # gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# # 礼帽：原始图像与进行开运算之后得到的图像的差。
# # tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# # 黑帽：进行闭运算之后得到的图像与原始图像的差。
# # blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# img = cv2.imread('j.jpg', 0)
# kernel = np.ones((3, 3), np.uint8)
# # img = sp_noise(img, 0.01)
# th1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# th2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# th3 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# th4 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# th5 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# images = [img, th1, th2, th3, th4, th5]
# titles = ['orig', 'MORPH_OPEN', 'MORPH_CLOSE', 'MORPH_GRADIENT', "MORPH_TOPHAT", "MORPH_BLACKHAT"]
# for i in range(6):
#     plt.subplot(2, 3, i + 1), plt.title(titles[i])
#     plt.imshow(images[i], cmap='gray'), plt.axis('off')
# plt.show()
#
pass  # ---------图像梯度/Sobel算子，Scharr算子，Laplacian 算子--------   2019-6-13 15:14:17
# # cv2.Sobel()， cv2.Schar()， cv2.Laplacian()
# img = cv2.imread('jgg2.jpg', 0)
# # cv2.CV_64F 输出图像度（数据类型）, 可以用-1， 与原图保持一致 np.uint8
# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# # 参数1， 0 为只在x方向求导数， 最大可以求2阶导数
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# # 参数0， 1 为只在y方向求导数， 最大可以求2阶导数
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# sobel = cv2.add(sobelx, sobely)
# images = [img, laplacian, sobelx, sobely, sobel]
# titles = ['orig', 'laplacian', 'sobelx', 'sobely', 'sobel']
# for i in range(5):
#     plt.subplot(2, 3, i + 1), plt.title(titles[i])
#     plt.imshow(images[i], cmap='gray'), plt.axis('off')
# plt.show()
#
#  -------图像深度与原图一致---------------------------------
# img = cv2.imread('jgg.jpg', 0)
# # Output dtype = cv2.CV_8U
# sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
# # 也可以将参数设为-1
# # sobelx8u = cv2.Sobel(img,-1,1,0,ksize=5)
# # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# abs_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)
# plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
# plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
# plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
# plt.show()
pass  # ---------Canny 边缘检测--------   2019-6-13 19:44:9
# #
# #
# def nothing(x):
#     pass
#
#
# img = cv2.imread('1.png', 0)
# cv2.namedWindow('Canny detection')
# cv2.createTrackbar('minVal', 'Canny detection', 0, 1000, nothing)
# cv2.createTrackbar('maxVal', 'Canny detection', 0, 1000, nothing)
# while 1:
#     minVal = cv2.getTrackbarPos('minVal', 'Canny detection')
#     maxVal = cv2.getTrackbarPos('maxVal', 'Canny detection')
#     edges = cv2.Canny(img, minVal, maxVal)
#     # plt.subplot(121), plt.imshow(img, cmap='gray')
#     # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#     # plt.subplot(122), plt.imshow(edges, cmap='gray')
#     # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#     # plt.show()
#     cv2.imshow('Canny detection', np.hstack([img, edges]))
#     k = cv2.waitKey(10)
#     if k == 27:
#         break
# cv2.destroyAllWindows()
pass  # ---------图像金字塔--------   2019-6-16 9:46:1
# 同一图像的不同分辨率的子图像处理，主要应用之一：图像融合
# 两类图像金字塔：高斯金字塔和拉普拉斯金字塔
# PS：图像融合过程中cv2.pyrUP 与 cv2.pyrDown 两个函数过程不可逆，且图像尺寸可能会有1个pix的变化
# lower_reso = cv2.pyrDown(higer_reso) # 尺寸变小，分辨率变小
# higher_reso2 = cv2.pyrUp(lower_reso) # 尺寸变大，分辨率不会增加
# img = cv2.imread('dingdang.jpg', 1)
# th1 = cv2.pyrDown(img)
# th2 = cv2.pyrUp(th1)
# th3 = img - th2
# cv2.imshow('gold', np.hstack([img, th2, th3]))
# cv2.imshow('temp', th1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # -------------图像融合-------------------
# A = cv2.imread('apple1.jpg')
# B = cv2.imread('orange1.jpg')
# # generate Gaussian pyramid for A,B
# GA = A.copy()
# GB = B.copy()
# gpA = [GA]
# gpB = [GB]
# # print(gpA[0].shape, gpB[0].shape)
# for i in range(6):
#     GA = cv2.pyrDown(GA)
#     GB = cv2.pyrDown(GB)
#     gpA.append(GA)
#     gpB.append(GB)
#     cv2.imshow('Gaussian', np.hstack((GA, GB)))
#     cv2.waitKey(10)
# # generate Laplacian pyramid for A,B
# lpA = [gpA[5]]
# lpB = [gpB[5]]
# for i in range(5, 0, -1):
#     GEA = cv2.pyrUp(gpA[i])
#     LA = cv2.subtract(gpA[i-1], GEA)
#     lpA.append(LA)
#     GEB = cv2.pyrUp(gpB[i])
#     LB = cv2.subtract(gpB[i-1], GEB)
#     lpB.append(LB)
#     cv2.imshow('Laplacian', np.hstack((LA, LB)))
#     cv2.waitKey(10)
#     # cv2.destroyAllWindows()
# # 将每一层的苹果左边与橘子右边进行拼接，拼接前需要确认两个图片尺寸一致
# LS = []
# for la, lb in zip(lpA, lpB):
#     rows, cols, dpt = la.shape
#     ls = np.hstack((la[:, 0:int(cols/2)], lb[:, int(cols/2):]))
#     LS.append(ls)
#     cv2.imshow('dst', ls)
#     cv2.waitKey(500)
#     # cv2.destroyAllWindows()
# # 开始重构，图片融合
# ls_ = LS[0]
# for i in range(1, 6):
#     ls_ = cv2.pyrUp(ls_)
#     ls_ = cv2.add(ls_, LS[i])
#     cv2.imshow('dst2', ls_)
#     cv2.waitKey(500)
#     # cv2.destroyAllWindows()
# rows, cols, dpt = A.shape
# real = np.hstack((A[:, :int(cols/2)], B[:, int(cols/2):]))
# cv2.imshow('real', real)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------轮廓--------   2019-6-16 15:57:29
# 轮廓可以简单认为成将连续的点（连着边界）连在一起的曲线，具有相同
# 的颜色或者灰度。轮廓在形状分析和物体的检测和识别中很有用。
# 1.为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理或者 Canny 边界检测。
# 2.查找轮廓的函数会修改原始图像。如果在找到轮廓之后还想使用原始图像的话，需将原始图像存储到其他变量中。
# 3.在 OpenCV 中，查找轮廓就像在黑色背景中找白色物体。要找的物体应该是白色而背景应该是黑色。
# def drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None,
# maxLevel=None, offset=None): # real signature unknown; restored from __doc__
# im = cv2.imread('zuiantu.jpg', 1)
# # im = cv2.imread('hb.jpg')
# img = im.copy()
# imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# # imgray = cv2.medianBlur(imgray, 5)
# cv2.namedWindow('gray')
# cv2.createTrackbar('minVal', 'gray', 0, 255, nothing)
# # cv2.createTrackbar('maxVal', 'gray', 0, 255, nothing)
# kernel = np.ones((3, 3), np.uint8)
# while 1:
#     minVal = cv2.getTrackbarPos('minVal', 'gray')
#     # maxVal = cv2.getTrackbarPos('maxVal', 'gray')
#     ret, thresh = cv2.threshold(imgray, minVal, 255, cv2.THRESH_BINARY)
#     # thresh = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
#     cv2.imshow('gray', thresh)
#     k1 = cv2.waitKey(10)
#     if k1 == 27:
#         break
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(im, contours, -1, (0, 255, 0), 1, offset=(0, 0))
# pass  # ----------- 矩， 轮廓的重心----------------------
# # cnt = contours[0]
# # # M 为矩的一个字典，包含
# # M = cv2.moments(cnt)
# # cx = int(M['m10']/M['m00'])
# # cy = int(M['m01']/M['m00'])
# # print(M, cx, cy)
# #
# cv2.imshow('orig-contours', np.hstack([img, im]))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------轮廓相关运算-------   2019-6-18 18:53:42
# ----------轮廓面积----计算公式 或 零阶矩
# cv2.contourArea(cnt)
# cnt = contours[0], M = cv2.moments(cnt)
# M['m00']
# ----------轮廓周长-------, True 闭合的， False 打开的
# perimeter = cv2.arcLength(cnt,True)
# ----------轮廓近似------------
# epsilon: 从原始轮廓到近似轮廓的最大距离, 这个参数用于调节轮廓的近似程度
# epsilon = 0.1 * cv2.arcLength(cnt, True)
# approx = cv2.approxPolyDP(cnt, epsilon, True)
# # ----------凸包------------
# 可以用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷
# hull = cv2.convexHull(cnt)
# # ----------凸性检测------
# 检测一个曲线是不是凸的， 是 True, 不是 False
# k = cv2.isContourConvex(cnt)
pass  # ---------边界矩形, 外接圆   -------   2019-6-18 19:49:24
# # # 直边界矩形，不会考虑对象是否旋转。（x，y）为矩形左上角的坐标，（w，h）是矩形的宽和高。
# # x, y, w, h = cv2.boundingRect(cnt)
# # 旋转的边界矩形, 考虑对象是否旋转, 面积最小。返回的是旋转矩形，cv2.boxPoints()可将其转换成矩形的四个角点坐标
# # cv2.minAreaRect(cnt), cv2.boxPoints(box)
# # 最小外接圆,对象的外切圆。面积最小。
# # (x,y),radius = cv2.minEnclosingCircle(cnt)
# # center = (int(x),int(y))
# # radius = int(radius)
# # img = cv2.circle(img,center,radius,(0,255,0),2)
# #
# img = cv2.imread('j.jpg')
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(img_g, 125, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
#
# # 直边界矩形
# x, y, w, h = cv2.boundingRect(cnt)
# img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# # 旋转的边界矩形
# pts = np.array(cv2.boxPoints(cv2.minAreaRect(cnt)), np.int32)
# img = cv2.polylines(img, [pts], True, (255, 0, 255), 2)
#
# # 最小外接圆
# (x, y), radius = cv2.minEnclosingCircle(cnt)
# center = (int(x), int(y))
# radius = int(radius)
# img = cv2.circle(img, center, radius, (255, 0, 0), 2)
#
# # 椭圆拟合, 返回值其实就是旋转边界矩形的内切圆
# ellipse = cv2.fitEllipse(cnt)
# img = cv2.ellipse(img, ellipse, (0, 255, 0), 2)
#
# # 直线拟合
# ows, cols = img.shape[:2]
# [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
# lefty = int((-x * vy / vx) + y)
# righty = int(((cols - x) * vy / vx) + y)
# img = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
#
# cv2.imshow('j', img)
# cv2.waitKey(0)
# cv2.destroyWindow()
pass  # ---------椭圆拟合，直线拟合-------   2019-6-18 20:32:55
# 返回值其实就是旋转边界矩形的内切圆(有可能只与两条边相切）
# ellipse = cv2.fitEllipse(cnt)
# img = cv2.ellipse(img,ellipse,(0,255,0),2)
# 图像中的白色点拟合出一条直线。
# rows, cols = img.shape[:2]
# [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
# lefty = int((-x * vy / vx) + y)
# righty = int(((cols - x) * vy / vx) + y)
# img = cv2.line(img, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
# 实例见上图
pass  # ---------轮廓性质-------   2019-6-19 14:45:1
#
# img = cv2.imread('j.jpg')
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(img_g, 125, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# # ---------极点  上下左右
# leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
# rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
# topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
# bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
# # ---------长宽比：边界矩形的宽高比 aspect_ratio
# x, y, w, h = cv2.boundingRect(cnt)
# aspect_ratio = float(w) / h
# # ---------轮廓面积与边界矩形面积的比  extent
# area = cv2.contourArea(cnt)
# x, y, w, h = cv2.boundingRect(cnt)
# rect_area = w * h
# extent = float(area) / rect_area
# # ---------轮廓面积与凸包面积的比  Solidity
# area = cv2.contourArea(cnt)
# hull = cv2.convexHull(cnt)
# # hull_area = cv2.contourArea(hull)
# # solidity = float(area) / hull_area
# # ---------与轮廓面积相等的圆形的直径  Equivalent Diameter
# area = cv2.contourArea(cnt)
# equi_diameter = np.sqrt(4 * area / np.pi)
# # ---------对象的方向，下面的方法会返回长轴和短轴的长度
# (x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
# print(MA, "go", ma)
# # ---------掩模和像素点
# mask = np.zeros(img_g.shape, np.uint8)
# # 这里一定要使用参数-1, 绘制填充的的轮廓
# cv2.drawContours(mask, contours, -1, 255, -1)
# cv2.imshow('mask', mask)
# cv2.waitKey(0)
# # cv2.ellipse(mask, (int(x), int(y)), (int(MA), int(ma)), angle, 0, 360, (255, 0, 255), 1)
# pixel_points = np.transpose(np.nonzero(mask))  # np.transpose 矩阵转置
# maskc = np.zeros(img.shape, np.uint8)
# for x, y in pixel_points:
#     maskc[x, y] = (255, 0, 255)
# cv2.imshow('maskc', maskc)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # ---------平均颜色及平均灰度-------   2019-6-19 14:45:1           平均灰度及颜色求法.....待解决
# img = cv2.imread('lf_H.jpg')
# img2 = img.copy()
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(img_g, 125, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#
# # img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img_hsv =img.copy()
#
# x1, y1 = -1, -1
# def draw_circle(event, x, y, flags, param):
#     """mouse callback function"""
#     global x1, y1, img2
#     mask = np.zeros(img_g.shape, np.uint8)
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         x1 = x
#         y1 = y
#     elif event == cv2.EVENT_RBUTTONDBLCLK:
#         cv2.rectangle(img, (x1, y1), (x, y), (255, 0, 0), 3)
#         mask[y1:y, x1:x] = 255  # 色度180 饱和度255 明度255
#
#         cv2.imshow('mask', mask)
#         cv2.waitKey(10)
#         mean_img = np.zeros((abs(x-x1),abs(y-y1),3), np.uint8)
#         for i in range(3):
#             mean_val = cv2.mean(img[:,:,i], mask=mask)                                         #   单通道处理！.......
#             print(mean_val)
#             print(img[:,:,i].shape)
#             img2[y1:y, x1:x,i] = int(mean_val[0]) #  区域ROI x,y 位置相反!!!!!!!!
#             mean_img[:,:,i] = int(mean_val[0])
#         cv2.circle(img, (x1, y1), 5, 255, 2)
#         cv2.circle(img, (x, y), 5, (0, 255, 0), 2)
#         cv2.imshow('mean_img', mean_img)
# # 创建图像与窗口并将窗口与回调函数绑定
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
# while 1:
#     cv2.imshow('image', img)
#     cv2.imshow('img2', img2)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()
pass  # ---------轮廓的层次结构-------   2019-7-1 21:28:30
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_LIST  提取所有的轮廓，而不去创建任何父子关系
# cv2.RETR_EXTERNAL 只返回最外边的的轮廓，所有的子轮廓都会被忽略掉。
# cv2.RETR_CCOMP  返回所有的轮廓并将轮廓分为两级组织结构。
# cv2.RETR_TREE 返回所有轮廓，并且创建一个完整的组织结构列表.
pass  # ---------直方图-------   2019-7-2 8:33:42
# # cv2.calcHist()，np.histogram()
# # cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# # 1. images: 原图像（图像格式为 uint8 或 float32）。当传入函数时应该
# # 用中括号 [] 括起来，例如：[img]。
# # 2. channels: 同样需要用中括号括起来，它会告诉函数我们要统计那幅图
# # 像的直方图。如果输入图像是灰度图，它的值就是 [0]；如果是彩色图像
# # 的话，传入的参数可以是 [0]，[1]，[2] 它们分别对应着通道 B，G，R。
# # 3. mask: 掩模图像。要统计整幅图像的直方图就把它设为 None。但是如
# # 果你想统计图像某一部分的直方图的话，你就需要制作一个掩模图像，并
# # 使用它。
# # 4. histSize:BIN 的数目。也应该用中括号括起来，例如：[256]。
# # 5. ranges: 像素值范围，通常为 [0，256]
#
# img = cv2.imread('girl.jpg', 1)
# # -------------OpenCV方法  运行速度是np方法的40倍!!!
# # 别忘了中括号 [img],[0],None,[256],[0,256]，只有 mask 没有中括号
# hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
#
# # -------------np 方法
# # img.ravel() 将图像转成一维数组，这里没有中括号。 channel需要通过图像本身获取
# hist_np, bins = np.histogram(img[:,:,0].ravel(), bins=256, range=[0, 256])
# plt.subplot(131)
# plt.plot(hist, color='r')
# plt.subplot(132)
# plt.plot(hist_np, color='g')
#
# # -------------matplotlib.plot.hist 方法
# plt.subplot(133)
# plt.hist(img[:,:,0].ravel(),256,[0,256])
# plt.show()
pass  # ---------直方图均衡化-------   2019-7-2 10:33:20
# # 将区域内灰度直方图分布平均化,增加灰度动态范围
# #
# img = cv2.imread('tt.jpg',1)
# img2 = np.zeros(img.shape, np.uint8)
# img3 = np.zeros(img.shape, np.uint8)
# channel = ('r', 'g', 'b')
# for i,color in enumerate(channel):    # enumerate 创建索引列及元素
#     #flatten() 将数组变成一维  返回源数据,ravel 不返回
#     hist,bins = np.histogram(img[:,:,i].flatten(),256,[0,256])
#     # plt.plot(hist, color = 'g')
#     # 计算累积分布图
#     cdf = hist.cumsum()
#     cdf_normalized = cdf * hist.max()/ cdf.max()
#     plt.plot(cdf_normalized, color = 'r')
#     plt.plot(hist, color=color)
#     # plt.hist(img[:,:,i].flatten(),256,[0,256], color = color)
#
#     # -------------构建 Numpy 掩模数组，cdf 为原数组，
#     # 当数组元素为 0 时，掩盖（计算时被忽略）。
#     cdf_m = np.ma.masked_equal(cdf,0)
#     cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
#     # 对被掩盖的元素赋值，这里赋值为 0
#     cdf = np.ma.filled(cdf_m,0).astype('uint8')
#     img2[:,:,i] = cdf[img[:,:,i]]
#
#     # ------------计算均衡化后的直方图和累积分布图
#     hist,bins = np.histogram(img2[:,:,i].flatten(),256,[0,256])
#     # plt.plot(hist, color = 'g')
#     # 计算累积分布图
#     cdf = hist.cumsum()
#     cdf_normalized = cdf * hist.max()/ cdf.max()
#     plt.plot(cdf_normalized, color = 'g')
#     plt.plot(hist, color=color)
#     # plt.hist(img2[:,:,i].flatten(),256,[0,256], color = color)
#
#     # ------------clahe 有限对比适应性直方图均衡化
#     #　自适应灰度直方图均衡化,减弱对比度变化较大的影响
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     img3[:,:,i] = clahe.apply(img[:,:,i])
#
#     # ------------计算均衡化后的直方图和累积分布图
#     hist, bins = np.histogram(img3[:, :, i].flatten(), 256, [0, 256])
#     # plt.plot(hist, color = 'g')
#     # 计算累积分布图
#     cdf = hist.cumsum()
#     cdf_normalized = cdf * hist.max() / cdf.max()
#     plt.plot(cdf_normalized, color='b')
#     plt.plot(hist, color=color)
#     # plt.hist(img3[:, :, i].flatten(), 256, [0, 256], color=color)
#
#     plt.xlim([0, 256])
#     plt.legend(('cdf', 'histogram'), loc='upper left')
#     plt.show()
#
# cv2.imshow('image', np.hstack([img, img2, img3]))
# # cv2.imwrite('tt_cdf.jpg', img2)
# cv2.waitKey(0)
#
# # -------------改变图像的亮度
# img = cv2.imread('tt.jpg', 0)
# img2 = np.zeros(img.shape, np.uint8)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img2[i,j] = 255 if 0.8*img[i,j] > 255 else int(0.8*img[i,j])
# cv2.imshow('compare', np.hstack([img, img2]))
# cv2.waitKey(0)
pass  # ---------直方图反向投影-------   2019-7-2 13:54:1
# # # 可以用来做图像分割，或者在图像中找寻我们感兴趣的部分。
# #
# # target is the image we search in
# target = cv2.imread('lf_H.jpg')
# hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
#
# # roi is the object or region of object we need to find
# roi = cv2.imread('good.jpg')
# # roi = target[100:200, 100:200,:]
# cv2.imshow('roi', roi)
# hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#
# # find the histograms using calcHist. Can be done with np.histogram2d also
# # calculating object histogram
# roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
#
# # normalize histogram and apply back projection 归一化
# cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
# # calcBackProject(images, channels, hist, ranges, scale, dst=None)
# dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
#
# #  cv2.getStructuringElement 构建一个椭圆的核
# disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# # cv2.filter2D  此处卷积可以把分散的点连在一起
# cv2.filter2D(dst,-1,disc,dst)
#
# # threshold and binary AND
# ret,thresh = cv2.threshold(dst,50,255,0)
# thresh = cv2.merge((thresh,thresh,thresh))
# res = cv2.bitwise_and(target,thresh)
# res = np.hstack((target,thresh,res))
# cv2.imshow('res.jpg',res)
# cv2.waitKey(0)
pass  # ---------图像傅里叶变换与逆变换-------  2019-7-2 19:34:16
# img = cv2.imread('ball.jpg',0)
#
# # 傅里叶变换在图像尺寸在2的指数时效率最高，数组的大小是 2，3，5 的倍数时效率较高，可以给图像补零实现
# rows,cols = img.shape
# nrows = cv2.getOptimalDFTSize(rows)
# ncols = cv2.getOptimalDFTSize(cols)
# nimg = np.zeros((nrows, ncols), np.uint8)
# nimg[:rows, :cols] = img
# print('rows,cols:',rows, cols,'  nrows, ncols:', nrows, ncols)
#
# # --------------OpenCv 中的傅里叶变换
# dft = cv2.dft(np.float32(nimg),flags = cv2.DFT_COMPLEX_OUTPUT)
# # 将直流分量平移到图像中间
# dft_shift = np.fft.fftshift(dft)
#
# # 双通道 dft_shift[:,:,0]为实部， dft_shift[:,:,1])为虚部
# # cv2.magnitude(x,y)  sqrt(x^2 +y^2)
# # magnitude_spectrum  幅值
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
# # 可选用cv2.cartToPolar同时获得幅值与相位
# # magnitude_spectrum, polar = cv2.cartToPolar(dft_shift[:,:,0],dft_shift[:,:,1])
# # cv2.imshow() 在两个图片深度不一样时显示会异常
# magnitude_spectrum = np.uint8(magnitude_spectrum)
# img_g = np.hstack([nimg, magnitude_spectrum])
# cv2.imshow('orig & DFT', img_g)
#
# # 在图像中央增加60*60 滤波窗口，过滤低频分量
# rows, cols = nimg.shape
# crow, ccol = int(rows/2) , int(cols/2)
# mask = np.ones((rows, cols,2), np.uint8)
# mask[crow-30:crow+30, ccol-30:ccol+30]=0
#
# # --------------增加滤波掩模
# fshift = dft_shift*mask    # 实行过滤
# f_ishift = np.fft.ifftshift(fshift)  # 平移回去
#
# # --------------OpenCv 中的傅里叶逆变换  2019-7-3 10:55:17
# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
#
# plt.imshow(img_back)
# plt.show()
# cv2.waitKey(0)
pass  # ---------模板匹配-------  2019-7-3 15:23:23
# # cv2.matchTemplate()   在一副大图中搜寻查找模版图像位置
# # cv2.minMaxLoc()  获取最小值和最大值的位置， 第一个值为矩形左上角的点（位置）
# # （w，h）为模板矩形的宽和高
#
# img = cv2.imread('ball.jpg', 0)
# img2 = img.copy()
# template = cv2.imread('moban.jpg', 0)
# w, h = template.shape[::-1]  # 逆序    h,w = template.shape
# print(template.shape)
# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# for meth in methods:
#     img  = img2.copy()
#     # exec 语句用来执行储存在字符串或文件中的 Python 语句。
#     # 例如，我们可以在运行时生成一个包含 Python 代码的字符串，然后使用 exec 语句执行这些语句。
#     # eval 语句用来计算存储在字符串中的有效 Python 表达式
#     method = eval(meth)
#
#     # 开始匹配并获取位置
#     res = cv2.matchTemplate(img, template, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     print(res.shape)
#     # 使用不同的比较方法，对结果的解释不同
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] +w, top_left[1]+h)
#     print(top_left, bottom_right)
#     # 加个矩形框显示出来
#     cv2.rectangle(img, top_left, bottom_right, 255, 2)
#
#     plt.subplot(121), plt.imshow(res, cmap='gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122), plt.imshow(img, cmap='gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#     plt.show()
pass  # ---------多对象的模板匹配-------  2019-7-3 20:12:29
# # 通过设定阈值对匹配结果进行筛选
# img_rgb = cv2.imread('mario.png')
# img = img_rgb.copy()
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template1 = cv2.imread('mario_coin.png',0)
#
# # 加边扩充测试对模板检测的影响
# w, h = template1.shape[::-1]
# template = np.zeros((h+10, w+10), np.uint8)
# template[:h, :w] =template1
# cv2.imshow('temp', template)
#
# # ---------多对象的模板匹配加阈值进行筛选
# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# #umpy.where(condition[, x, y])
# #Return elements, either from x or y, depending on condition.
# #If only condition is given, return condition.nonzero().
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
# cv2.imshow('find_coins',np.hstack([img, img_rgb]))
# cv2.waitKey(0)
pass  # ---------OpenCV 中的霍夫变换-------  2019-7-3 21:46:3
# # 直线方程由 rho, theta 可确定x*cos(theta) + y*sin(theta) - rho = 0
# # 创建一个 2D 数组（累加器），初始化累加器，所有的值都为 0。行表示 rho，列表示 theta
# # 对图像进行二值化，对图像上的非零像素进行遍历，对于某像素（x,y）,寻找使直线方程成立的rho,theta对，并在2D数据累加1
# img = cv2.imread('jgg.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 30, 150, apertureSize=3)
# cv2.imshow('e', edges)
#
# # HoughLines(image, rho, theta, threshold)  rho theta 为相应参数分辨率
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)
#
# for rho, theta in lines[:,0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#     x1 = int(x0 + 1000 * (-b))
#     y1 = int(y0 + 1000 * (a))
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * (a))
#     cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
# cv2.imshow('houghlines3.jpg', img)
# cv2.waitKey(0)
pass  # ---------模板的创建与检测-------  2019-7-4 10:9:36
# 根据一张原图找出ROI并创建模板，利用创建的模板对其他图片进行匹配
#
# def axis_pick(event, x, y, flags, param):
#     """获取鼠标点击坐标，确定ROI区域"""
#     global x1, y1, x2, y2, axis_Nm, img2
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         x1, y1 = x,y
#         axis_Nm = 1
#         cv2.circle(img2, (x,y),2, (255,0,0), -1)
#     elif event == cv2.EVENT_RBUTTONDBLCLK and axis_Nm == 1 :
#         x2, y2 = x, y
#         axis_Nm = 2
#         cv2.circle(img2, (x,y),2, (0,0,255), -1)
#
# # 找一幅图并选择创建模板
# def model_creat(img_g, type):
#     """
#     创建模板
#     :param img_g: input src
#     :param type:  model type : circle, rectangle
#     :return: model img
#     """
#     global img2 , radius
#     cv2.namedWindow('model creat', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
#     cv2.waitKey(10)
#     cv2.setMouseCallback('model creat', axis_pick)
#     while 1:
#         cv2.imshow('model creat', img2)
#         key = cv2.waitKey(1)
#         if key == 27:
#             break
#     if type == 'circle':   #　circle 点水平直径
#         radius = int(abs((x2-x1)/2))
#         temp = img_g[(y1-radius):(y2+radius), x1:x2]
#     elif type == 'rectangle':  #　rectangle 点对角
#         temp = img_g[y1:y2, x1:x2]
#
#     return temp
#
# # 模板类型
# TYPE = 'circle'
# img = cv2.imread('E:\AOI_test\src\ (1).png')
# # img = cv2.imread('DetectCirclesExample_01.png')
#
# img2 = img.copy()
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 调用模板创建函数生成模板
# template = model_creat(img_g, TYPE)
# w, h = template.shape[::-1]
#
# cv2.imshow('template',template)
# # 使窗口可以按比例拉伸
# cv2.namedWindow('result', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
# for i in range(1,20):
#     img_target = cv2.imread(r'E:\AOI_test\src\ ('+str(i)+').png')
#     # img_target = cv2.imread('DetectCirclesExample_01.png')
#     res = cv2.matchTemplate(img_target[:,:,0],template,cv2.TM_CCOEFF_NORMED)
#
#     # # 单对象匹配，只需得分最高的匹配项
#     # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     # if TYPE == 'circle':
#     #     cv2.circle(img_target, (max_loc[0] + radius, max_loc[1] + radius), radius, (0, 255, 0), 3)
#     # elif TYPE == 'rectangle':
#     #     cv2.rectangle(img_target, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 3)
#     #
#     #
#     # 多对象匹配
#     threshold = 0.8
#     #Return elements, either from x or y, depending on condition.
#     #If only condition is given, return condition.nonzero().
#     loc = np.where( res >= threshold)
#     for pt in zip(*loc[::-1]):
#         if TYPE == 'circle':
#             cv2.circle(img_target, (pt[0]+radius, pt[1]+radius), radius, (0, 255, 0), 2)
#         elif TYPE == 'rectangle':
#             cv2.rectangle(img_target, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
#
#     cv2.imshow('result', img_target)
#     k = cv2.waitKey(0)
#     if k == 27:
#         break
pass  # ---------Hough 圆环变换-------  2019-7-4 15:31:17
#   不起作用哦，后面再来研究你!!!
#
# img = cv2.imread('2.jpg', 0)
#
# img = cv2.medianBlur(img,5)
# cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#
# # edges = cv2.Canny(img, 200, 500)
# cv2.imshow('img',np.hstack([img]))
# print("let's go")
# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                            param1=50,param2=30,minRadius=0,maxRadius=0)
# circles = np.uint16(np.around(circles))
# print("hi, I'm here")
# for i in circles[0,:]:
#     if 0<i[2]<30  :
#         # draw the outer circle
#         cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#         # draw the center of the circle
#         cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
# cv2.namedWindow('cimg', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
# cv2.imshow('cimg', cimg)
# cv2.waitKey(0)
pass  # --------分水岭图像分割 ------  2019-7-5 9:49:1
#
# # img1 = cv2.imread('DetectCirclesExample_01.png', 0)
# img = cv2.imread('coin.jpg')
# img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Otsu’s 二值化
# ret, thresh = cv2.threshold(img_g, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# cv2.imshow('Otsu' ,thresh)
#
#
# # 开运算，先腐蚀后膨胀 去除背景中的噪点
# kernel = np.ones((3,3), np.uint8)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)  # iterations=2 连续做2次
# cv2.imshow('opening' ,opening)
#
# # 对图膨胀，剩下的是确定的背景区域
# sure_bg = cv2.dilate(opening, kernel, iterations=3)
# cv2.imshow('sure_bg' ,sure_bg)
# # ------------距离变换，含义为计算图像中非零像素点到最近零像素点的距离
# # 根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
# dist_transform = cv2.distanceTransform(opening,1,5)
# ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(), 255, cv2.THRESH_BINARY)
#
# # # 显示下距离变换结果
# # dist_transform = dist_transform*(255/dist_transform.max()) # 太暗，亮度等比例放大，最亮的放大到255
# # dist_transform = np.uint8(dist_transform)
# # cv2.imshow('dist_transform' ,dist_transform)
#
# # 找出未知区域，后续采用分水岭检测
# sure_fg = np.uint8(sure_fg)
# unknown = cv2.subtract(sure_bg, sure_fg)   # 矩阵减法 sure_bg - sure_fg
# # unknown2 = sure_bg - sure_fg   # 和上式等价，上式执行效率更高,约为2倍
# cv2.imshow('unknown' ,unknown)
#
# # Marker labelling 对图象中的对象做标记
# # cv2.connectedComponents(src) 将图中背景标记为0，其他对象按顺序标记为1，2，3...
# ret, markers1 = cv2.connectedComponents(sure_fg)
# # markers1 = np.uint8(markers1)
# # cv2.imshow('markers1' ,markers1)
# # Add one to all labels so that sure background is not 0, but 1
# markers = markers1+1
#
#
# # cv2.imshow('markers' ,markers)
# # Now, mark the region of unknown with zero  看到没有！ 矩阵元素可以通过加表达式来进行选择！！！
# markers[unknown==255] = 0
# plt.imshow(markers)
# plt.show()
# # -------咚咚咚  分水岭图像分割 边界会被标记为-1 对象标记为1 markers3内元素是bool变量
# markers3 = cv2.watershed(img,markers)
# img[markers3 == -1] = [255,0,0]
# cv2.imshow('img' ,img)
#
# cv2.waitKey(0)
pass  # --------角点检测 ------  2019-7-5 14:43:51
# # cv2.cornerHarris()
# # • img - 数据类型为 float32 的输入图像。
# # • blockSize - 角点检测中要考虑的领域大小。
# # • ksize - Sobel 求导中使用的窗口大小
# # • k - Harris 角点检测方程中的自由参数，取值参数为 [0,04，0.06].
# filename = 'zhiheren.jpg'
# img = cv2.imread(filename)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# # 输入图像必须是 float32，最后一个参数在 0.04 到 0.05 之间
# dst = cv2.cornerHarris(gray,2,3,0.04)
# #result is dilated for marking the corners, not important
# dst = cv2.dilate(dst,None)
# # Threshold for an optimal value, it may vary depending on the image.
# img2 = img.copy()
# img2[dst>0.01*dst.max()]=[0,0,255]
# cv2.imshow('dst general',img2)
# # cv2.waitKey(0)
#
# # --------亚像素角点检测 ------  2019-7-5 17:14:0
# ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
# dst = np.uint8(dst)
# cv2.imshow('dst',dst)
# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
#
# # define the criteria to stop and refine the corners 定义停止条件并提取角点
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# # 返回值由角点坐标组成的一个数组（而非图像）
# corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
#
# # Now draw them
# res = np.hstack((centroids,corners))
# #np.int0 可以用来省略小数点后面的数字（非四㮼五入）。
# res = np.int0(res)
# img[res[:,1],res[:,0]]=[0,0,255]         # 瞅瞅，快来瞅瞅，又一种矩阵元素操作！！！
# img[res[:,3],res[:,2]] = [0,255,0]
# cv2.namedWindow('subpixel5.png', cv2.WINDOW_NORMAL|cv2.WINDOW_KEEPRATIO)
# cv2.imshow('subpixel5.png',img)
# cv2.waitKey(0)
pass  # --------Shi-Tomasi 角点检测 & 适合于跟踪的图像特征 ------  2019-7-6 9:24:46
# # 输入的应该是灰度图像
# # 想要检测到的角点数目。再设置角点的质量水平，0到 1 之间。它代表了角点的最低质量，低于这个数的所有角点都会被忽略。
# # 最后在设置两个角点之间的最短欧式距离。  R = min( 人1 ， 人2）
# # cv2.goodFeatureToTrack(image, maxCorners, qualityLevel, minDistance)
#
# img = cv2.imread('zhiheren.jpg')
# img2 = img.copy()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # 进行角点检测， 返回的是检测到角点的坐标[[[x1,y1]] [[x2,y2]] ...]
# corners = cv2.goodFeaturesToTrack(gray, 20, 0.51, 20)
# corners = np.int0(corners)  # 舍弃小数部分
# print(corners[:3])
# for i in corners:
#     x,y = i.ravel()
#     cv2.circle(img, (x,y), 3, (0,0,255), -1)
#
# cv2.imshow('corner detected result', np.hstack([img2, img]))
# cv2.waitKey(0)


