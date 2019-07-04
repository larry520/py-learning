import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


print(r'E:\AOI_test\src\ ('+str(1)+').png')
img = cv2.imread(r'E:\AOI_test\src\ ('+str(1)+').png')
cv2.imshow('f', img)
cv2.waitKey(0)