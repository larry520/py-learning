import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import tensorflow as tf
import matplotlib.pyplot as plt
import os


a = list(range(9))
print(a)

a = np.reshape(a,(3,3))
print(a)

a[:,2]=255
print(a)