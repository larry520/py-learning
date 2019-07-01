# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
from PIL import Image


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
#
#
# def nothing(x):
#     pass
#
#
# img = cv2.imread('girl.jpg', 0)
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

img = cv2.imread('j.jpg')
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_g, 125, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# ---------长宽比：边界矩形的宽高比 aspect_ratio
x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w) / h
# ---------轮廓面积与边界矩形面积的比  extent
area = cv2.contourArea(cnt)
x, y, w, h = cv2.boundingRect(cnt)
rect_area = w * h
extent = float(area) / rect_area
# ---------轮廓面积与凸包面积的比  Solidity
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
# hull_area = cv2.contourArea(hull)
# solidity = float(area) / hull_area
# ---------与轮廓面积相等的圆形的直径  Equivalent Diameter
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4 * area / np.pi)
# ---------对象的方向，下面的方法会返回长轴和短轴的长度
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print(MA, "go", ma)
# ---------掩模和像素点
mask = np.zeros(img_g.shape, np.uint8)
# 这里一定要使用参数-1, 绘制填充的的轮廓
cv2.drawContours(mask, contours, -1, 255, -1)
cv2.imshow('mask', mask)
cv2.waitKey(0)
# cv2.ellipse(mask, (int(x), int(y)), (int(MA), int(ma)), angle, 0, 360, (255, 0, 255), 1)
pixel_points = np.transpose(np.nonzero(mask))  # np.transpose 矩阵转置
maskc = np.zeros(img.shape, np.uint8)
for x, y in pixel_points:
    maskc[x, y] = (255, 0, 255)
cv2.imshow('maskc', maskc)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('good job！')