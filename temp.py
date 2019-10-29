import numpy as np

s = {'1':1,'2':2}
sc = s.copy()
s['1'] = 5
sum = s['1'] + sc['1']
print(sum,[12]+[13])

a = np.repeat(np.arange(5).reshape([1,-1]),10,axis=0)
print(a)

