# import numpy as np
import time,datetime


# s = {'1':1,'2':2}
# sc = s.copy()
# s['1'] = 5
# sum = s['1'] + sc['1']
# print(sum,[12]+[13])
#
# a = np.repeat(np.arange(5).reshape([1,-1]),10,axis=0)
# print(a)
#
# class demo(object):
#
#     def __init__(self):
#         self.a = 10
#         self.d = 1
#         b = 20
#     def test1(self,k):
#         c = 30
#         self.d = 40
#         print(self.a,k)
#     @property
#     def d(self):
#         return self.d
#     @d.setter
#     def d(self, value):
#         sefl.d = value
#     def test2(self):
#         sum = self.a +self.d
#
#
# A = demo
# B = demo
# A.d = 10
# print(A.d)
#
# print(type(datetime.datetime.now().strftime("%H:%M:%S")))
# print(type("good"))
#
# t1 = datetime.datetime.now().strftime("%Y-%m-%d") +" 23:01:00"
# time.sleep(1)
# t2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# if t1>t2:
#     print(t1, t2)
#
# stra = "12:33,12:20"
# strb = stra.split(',')
# print(strb)
# t = time.time()
# t2 = datetime.datetime.now()
# t3 = t - t2
# print(t, t2, t3)


a =3.1314526
b = "%.3f" %float("%.5f" % a)
print(b,type(b))

print(datetime.datetime.now())
bindFuncs = "[2,5,]"
t1 = bindFuncs.replace(";", ",").replace('[', '["')
t2 = t1.replace(',', '","')
t3=t2.replace(',"]', ']')
bindFuncList = eval(t3)
print(t1,t2,t3)
print(type(t1),type(t2),type(t3),bindFuncs)

print( 3<4<5)
