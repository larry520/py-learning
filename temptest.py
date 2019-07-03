import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mat = np.zeros((100,50,3))
mat[60:80, 40:50]=[255, 0,0]
cv2.rectangle(mat,(40,60), (50,80), (255,0,255),3)

cv2.imshow('mag',mat)
cv2.waitKey(0)