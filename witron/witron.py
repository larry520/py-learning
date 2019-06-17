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
img1 = cv2.imread('1_1.png', 0)
img2 = cv2.imread('1_2.png', 0)
cv2.namedWindow('dst')
cv2.createTrackbar('alfa', 'dst', 0, 100, nothing)
while 1:
    alfa = cv2.getTrackbarPos('alfa', 'dst')
    # dst = cv2.add(img1, img2)
    dst = cv2.addWeighted(img1, 1-alfa/100, img2, alfa/100, 0)
    # 将两张图中对应位置亮度较小的像素生成一个新图
    dst = np.minimum(img1, img2)
    cv2.imshow('dst', np.hstack([img1, img2, dst]))
    k = cv2.waitKey(10)
    if k == 27:
        cv2.imwrite('zuiantu.jpg', dst)
        break
cv2.destroyAllWindows()



