#
# x = [4, 5]
# y = [1, 2, 3]
# # x.append(y)  # x: [1, 2, 3, [4, 5]]
# # print(x)
# x.extend(y)
# print(x)
# #  排序 sort
# x.sort()
# print(x)

# 创建字典方式
# a = {'one': 1, 'two': 2, 'three': 3}
# b = dict(one=1, two=2, three=3)
# c = dict([('one', 1), ('two', 2), ('three', 3)])
# d = dict(zip(['onea', 'twoa', 'threea'], [1, 2, 3]))
# e = dict({'one': 1, 'two': 2, 'three': 3})
# print(a == b == c == d == e)
#
#
# def print_n(x, y, *kw):  # *kw接受多个参数，自动构成一个tuple, **kw 构成一个dict
#     print(x, y, kw)
#
#
# print_n(a, b, c, *d)  # c 将整个dict作为tuple的一个元素，*d将每个dict关键字作为元素
#
#
# def fact(n):
#     return fact_iter(n, 1)
#
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num-1, num*product)
#
#
# print(fact(100))


# class Dog():
#     """一次模拟小狗的尝试"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗蹲下"""
#         print(self.name.title()+" is now sitting ")
#
#
# class EHa(Dog):
#     """这是一条二哈"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("一条新的二哈 ")
#
#     def rollover(self):
#         print(self.name + " biubiubiu~")
#
#
# class Bai(EHa):
#     """这是一条白毛二哈"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("一条新的白毛二哈 ")
#
#     def Wa(self):
#         print(self.name + " Hiahiahia~")
#
# Hak = Bai("xiaobao", 2)
# Hak.sit()
# Hak.Wa()
# print(Hak.name)

# import time
# import calendar
#
# localtime = time.asctime(time.localtime(time.time()))
# print("本地时间：", localtime)
#
# print(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
#
# cal = calendar.month(2019, 5)
# print("2019年5月日历：\n", cal)

# import re
#
# a = re.match(r'[a-zA-Z_][a-z|A-Z1-9_]+@[a-zA-Z1-9]+\.[a-zA-Z1-9]+', 'ab@dfaddf.com')
# print(a, "\n")
# print("-------------------我是分隔符-------------------")
# b = re.search(r'd.*', 'ab@dfaddf.com')
# print(b, "\n")
#
# # 正则表达式中，
# # # *表示任意个字符（包括0个）
# # # +表示至少一个字符
# # # ?表示0个或1个字符
# # # {n}表示n个字符
# # # {n,m}表示n-m个字符
# # \d可以匹配一个数字
# # \D可以匹配不是数字的字符
# # \w可以匹配一个字母或数字
# # \W可以匹配不是字母或数字的字符
# # \s可以匹配一个空格（也包括Tab等空白符）
# # \S可以匹配非空格字符
# # []表示范围,[0-9a-z\_]可以匹配一个数字或字母或下划线
# # A|B可以匹配A或B
# # 由于\d+采用贪婪匹配，加？可实现非贪婪匹配
# # ^表示行的开头，^\d表示必须以数字开头。
# # $表示行的结束，\d$表示必须以数字结束。
# # re.match(patten,repl,string,flags=0) 只匹配字符串的开始，如果开始不符正则表达式，则匹配失败
# # re.search(patten,repl,string,flags=0) 匹配整个字符串，直到找到一个匹配
# # re.sub(patten,repl,string,count=0,flags=0) 匹配字符串并用给定内容替换
# # re.compile(patten[,flags] 预编译，给match search sub使用
#
# # pattern = re.compile(r'\d+') #  用于匹配至少一个数字
# # m = pattern.match('one12three34four') # 查找头部，没有匹配
#
# phone = "2004-959-559 #  这是一个国外电话号码"
# qt = re.compile(r'\w+')
# st = 'runoob, runoob, runoob.'
# nmt = re.sub(r'\.', "", st)
# nm = re.split(',', nmt)
# print(nm)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.stats import binom, norm, beta, expon
# a = np.zeros((3, 4))
# b = np.random.rand(2, 3, 4)
# c = np.eye(4, 3)
#
# d = np.arange(1, 13, 1)
# f = d.reshape(3, 4)
# g = f.T
# h = np.matmul(f,g)
# i = f*f
# print(i, "\n------------\n", f)

# b = [list(range(0, 5)), list(range(10, 15))]
# bmn = np.mean(b)  # 全部元素求平均
# bm = np.mean(b, 0)  # 按列求平均
# bn = np.mean(b, 1)  # 按行求平均
# print(bmn, bm, bn)
# bvar = np.var(b)
# bmvar = np.std(b, 0)
# bnvar = np.std(b, 1)
# print(bvar, bmvar, bnvar)

# x = np.random.poisson(lam=5, size=10000)
# a = plt.hist(x, bins=15, density=True, range=[0, 15], alpha=0.5)
# plt.plot(a[1][0:15], a[0], 'g')
# plt.show()

# sigma = 1
# mu = 0
# x = np.arange(-5, 5, 0.1)
# y = norm.pdf(x, mu, sigma)  # 正太分布函数
# plt.plot(x, y, 'r')
# plt.title('Normal distribution')
# plt.xlabel('x')
# plt.ylabel('density')
# plt.show()

x = np.linspace(0, 1, 11)
print(x)