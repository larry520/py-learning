# -*- encoding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def welcome():
    print('welcome to my word!')


welcome()
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')
plt.title("simple plot")
plt.legend()
plt.show()
