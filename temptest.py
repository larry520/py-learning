import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

img = cv2.imread('girl.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
fig = plt.figure()
ax = Axes3D(fig)
Y1 = np.arange(0,180,1)
X1 = np.arange(0,256,1)
X1, Y1 = np.meshgrid(X1, Y1)
ax.plot_surface(X1, Y1, hist, rstride=1, cstride=1, cmap='rainbow')
plt.show()
