import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


pass  # 选择合适的方法识别胶水轨迹
# img = cv2.imread('2.jpg', 1)
# # 对图像进行中预处理，中值滤波
# # img = cv2.medianBlur(img, 3)
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow('Gray test')
# cv2.createTrackbar('Gray', 'Gray test', 0, 255, nothing)
# bg_img = np.zeros(img.shape, np.uint8)
# bg_img[:, :] = [0, 0, 255]
# while 1:
#     Gray_V = cv2.getTrackbarPos('Gray', 'Gray test')
#     # 使用简单阈值法
#     ret, mask1 = cv2.threshold(img1, Gray_V, 255, cv2.THRESH_BINARY)
#     kernel = np.ones((5, 5), np.uint8)
#     # 使用闭运算可使小黑点忽略掉
#     # mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)
#
#     # 使用自适应阀值法在某些场合效果很差
#     # mask1 = cv2.adaptiveThreshold(img1, Gray_V, cv2.ADAPTIVE_THRESH_MEAN_C,
#     #                               cv2.THRESH_BINARY, 3, 2)
#     # mask1 = cv2.adaptiveThreshold(img2, Gray_V, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     #                               cv2.THRESH_BINARY, 3, 2)
#     img_bg = cv2.bitwise_and(img, img, mask=mask1)
#     mask_inv = cv2.bitwise_not(mask1)
#     th1 = cv2.bitwise_and(bg_img, bg_img, mask=mask_inv)
#     img_fg = cv2.bitwise_and(bg_img, th1)
#     img_ok = cv2.add(img_bg, img_fg)
#     cv2.imshow('Gray test', np.hstack([mask1, mask_inv]))
#     cv2.imshow('img_bg', np.hstack([img, img_ok]))
#     k = cv2.waitKey(10)
#     if k == 27:
#         break
# cv2.destroyAllWindows()
pass  # 拟合最暗图
im1 = cv2.imread('1_1.png', 1)
im1c = im1.copy()
im2 = cv2.imread('1_2.png', 1)
im2c = im2.copy()
im1gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
img1 = cv2.medianBlur(im1gray, 3)
img2 = cv2.medianBlur(im2gray, 3)
# 将两张图中对应位置亮度较小的像素生成一个新图
dst = np.minimum(im1, im2)
dstc = dst.copy()
# cv2.imshow('dst', np.hstack([img1, img2, dst]))
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()
pass  # 寻找轮廓
cv2.namedWindow('Canny detection')
cv2.createTrackbar('minVal', 'Canny detection', 0, 255, nothing)
# while 1:
#     minVal = cv2.getTrackbarPos('minVal', 'Canny detection')
#     ret, thresh1 = cv2.threshold(img1, minVal, 255, cv2.THRESH_BINARY)
#     ret, thresh2 = cv2.threshold(img2, minVal, 255, cv2.THRESH_BINARY)
#     thresh3 = cv2.bitwise_and(thresh1, thresh2)
#     cv2.imshow('Canny detection', np.hstack([thresh1, thresh2, thresh3]))
#     k = cv2.waitKey(10)
#     if k == 27:
#         break
# contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours2, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours3, hierarchy = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 对找到的轮廓加面积判断，处理噪点影响
cv2.namedWindow('areaVal adjust')
cv2.createTrackbar('areaVal', 'areaVal adjust', 0, 400, nothing)

while 1:

    minVal = cv2.getTrackbarPos('minVal', 'Canny detection')
    ret, thresh1 = cv2.threshold(img1, minVal, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img2, minVal, 255, cv2.THRESH_BINARY)
    thresh3 = cv2.bitwise_and(thresh1, thresh2)
    cv2.imshow('Canny detection', np.hstack([thresh1, thresh2, thresh3]))
    contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours3, hierarchy = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areaVal = cv2.getTrackbarPos('areaVal', 'areaVal adjust')
    contours = [contours1, contours2, contours3]
    q = 0
    # 直接对原来列表过滤生成新的列表
    for i in range(len(contours)):
        contours[i] = [x for x in contours[i] if cv2.contourArea(x) > areaVal]
    # # 采用倒序循环方式遍历列表删除元素
    # for j in range(len(contours)-1, -1, -1):
    #     for i in range(len(contours[j])-1, -1, -1):
    #         areaV = cv2.contourArea(contours[j][i])
    #         if areaV < areaVal:
    #             del contours[j][i]

    cv2.drawContours(im1, contours[0], -1, (0, 255, 0), 1, offset=(0, 0))
    cv2.drawContours(im2, contours[1], -1, (0, 255, 0), 1, offset=(0, 0))
    cv2.drawContours(dst, contours[2], -1, (0, 255, 0), 1, offset=(0, 0))
    cv2.imshow('cout', dst)
    cv2.imshow('contours', np.hstack([im1, im2]))
    k = cv2.waitKey(10)
    if k == 27:
        break
    cv2.destroyWindow('cout')
    cv2.destroyWindow('contours')
    im1 = im1c.copy()
    im2 = im2c.copy()
    dst = dstc.copy()
cv2.destroyAllWindows()


