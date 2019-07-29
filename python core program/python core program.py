# -*- encoding: utf-8 -*-

# 代码风格：
"""
1. 起始行
通常只有在类 Unix 环境下才使用起始行，有起始行就能够仅输入脚本名字来执行脚本，无
需直接调用解释器。
2. 模块文档
简要介绍模块的功能及重要全局变量的含义，模块外可通过 module.__doc__ 访问这些内容。
3.  模块导入
导入当前模块的代码需要的所有模块；每个模块仅导入一次（当前模块被加载时）；函数
内部的模块导入代码不会被执行， 除非该函数正在执行。
4. 变量定义
这里定义的变量为全局变量，本模块中的所有函数都可直接使用。从好的编程风格角度说，
除非必须，否则就要尽量使用局部变量代替全局变量，如果坚持这样做，你的代码就不但容易
维护，而且还可以提高性能并节省内存。
5. 类定义语句
所有的类都需要在这里定义。当模块被导入时 class 语句会被执行, 类也就会被定义。类
的文档变量是 class.__doc__。
6. 函数定义语句
此处定义的函数可以通过 module.function()在外部被访问到，当模块被导入时 def 语句
会被执行， 函数也就都会定义好，函数的文档变量是 function.__doc__。
7. 主程序
无论这个模块是被别的模块导入还是作为脚本直接执行，都会执行这部分代码。通常这里
不会有太多功能性代码，而是根据执行的模式调用不同的函数。
"""

import numpy as np
import copy
from functools import wraps
import os

ls = os.linesep

# print('-' * 20, 'Hello World!', '-' * 20)
# print(1<<2)
pass  # ---------切片对象
# # sequence[start1 : end1, start2 : end2]
# # sequence[...,start1 : end1 ]
# # sequence[起始索引 : 结束索引 : 步进值]
# sequence = np.eye(5)
# sequence = sequence*np.array(list(range(1,6)))
# I1 = sequence[1:3,0:5]
# print(I1)
# foostr = '123456789'
# print(foostr[::],foostr[::2],foostr[::-1],foostr[::-2],
#       foostr[1::2], foostr[1:5:2], foostr[1:-1], foostr[1:-2])
pass
# repr(obj) 或 `obj` 返回一个对象的字符串表示 repr() 与 ''功能完全一样
# str(obj) 返回对象适合可读性好的字符串表示
pass  # ---------复数 i 用 j 或 J 来表示
# # num.real 该复数的实部  浮点类型
# # num num.imag  该复数的虚部  浮点类型
# # num.conjugate() 返回该复数的共轭复数
# a = 2 + 3j
# b = 3
# c = a +b
# print(c, c.real, c.imag, c.conjugate())
pass  # ---------深拷贝copy.deepcopy()与浅拷贝.copy [:]
# alist = [1, ['a', 'b']]
# blist = alist  # 引用,指向同一个list
# clist = alist[:]  # 浅拷贝
# # 浅拷贝  作用同 blist = alist.copy()
# # 对于列表中的元素为容器情形只拷贝容器地址
# dlist = copy.deepcopy(alist)  # 深拷贝
# print(alist, blist, clist, dlist)
# alist[0] = 'wa'
# alist[1][1] = 'c'
# print(alist, blist, clist, dlist)
pass  # ----------字典 dict 应用 2019-7-15 16:2:0
#
# d = dict.fromkeys(['a1', 'a3'], 10)
# print(d)
# d = dict.fromkeys(['a1', 'a2', 'a3'], [1, 2, 3])
# print(d)
#
pass  # ----------&,|,and, or-----------2019-7-17 10:49:26
# &,  |：
# # 1&2，2在二进制里面是10,1在二进制中是01，那么01与运算10得到是0
# 1 & 2         # 输出为 0，
# 1 | 2          # 输出为3
#
# and, or:
#  # 判断变量是否为0， 是0则为False，非0判断为True，
#  # and中含0，返回0； 均为非0时，返回后一个值，
# 2 and 0   # 返回0
# 2 and 1   # 返回1
# 1 and 2   # 返回2
#
# # or中， 至少有一个非0时，返回第一个非0,
# 2 or 0   # 返回2
# 2 or 1   # 返回2
# 0 or 1   # 返回1
pass  # ----------异常处理---------------2019-7-19 9:32:3
# """伪代码说明log作用，异常或成功信息记录"""
# import 3rd_party_module
# log = open('logfile.txt', 'w')
# try:
#     3rd_party_module.function()
# except:
#     log.write("*** caught exception in module\n")
# else:
#     log.write("*** no exceptions caught\n")
# log.close()
# # ---------断言表达式
# try:
#     assert 1 == 0
# except AssertionError:
#     print('assert error')
#
# def safe_float(obj):
#     try:
#         retval = float(obj)
#     # except BaseException:   # 所有异常都屏蔽了， 可能会错过关注的异常
#     except (TypeError, ValueError):  # 处理特定的异常
#         print('warning: argument must be a number or numeric string')
#         retval = None
#     return retval
pass  # ----------多线程---------------2019-7-19 13:51:28
# #Thread对象函数 描述
# # start()  开始线程的执行
# # run()  定义线程的功能的函数（一般会被子类重写）
# # join(timeout=None) 程序挂起，直到线程结束；如果给了 timeout，则最多阻塞 timeout 秒
# # getName()  返回线程的名字
# # setName(name)  设置线程的名字
# # isAlive()  布尔标志，表示这个线程是否还在运行中
# # isDaemon()  返回线程的 daemon 标志
#

# import threading
# import datetime
# import time
#
#
# def print_time(therading, state=''):
#     print(therading, state, 'at:', datetime.datetime.now())
#
#
# def loop0():
#     print_time("loop0", 'start')
#     time.sleep(3)
#     print_time("loop0", 'end')
#
#
# def loop1():
#     print_time('loop1', 'start')
#     time.sleep(6)
#     print_time('loop1', 'end')
#
#
# try:
#     thread1 = threading.Thread(target=loop0)
#     thread2 = threading.Thread(target=loop1)
#     threads = [thread1, thread2]
#     print_time('Main thread start')
#     for t in threads:
#         t.start()      # 启动线程
#         time.sleep(0.001)
#         print(threading.Thread.getName(t))   # thread name 并不是thread1 默认为 Thread-1
#     for t in threads:
#         t.join()       # 等待线程结束 join(n)表示阻塞n秒,n= 0时等待所有线程结束
#     print_time('all thread done')
# except ValueError:
#     print("Error: 无法启动线程")
pass  # ----------函数式编程 装饰器---------------2019-7-22 16:4:46
#
#
# def a_new_decorator(a_func):
#     #  以下文本内容可通过 foo.__doc__ 引用
#     """
#     example for decorator
#     :param a_func:  a function
#     :return:
#     """
#     @wraps(a_func)   # 使得装饰器内的函数的名字与文档得以保留
#     def wapTheFunction():
#         print('do something before executing a_func()')
#         a_func()
#         print('do something after executing a_func()')
#     return wapTheFunction
#
#
# # 装饰器的作用等价于 a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# @a_new_decorator
# def a_function_requiring_decoration():
#     print('需要用装饰器做一些处理的函数')
#
#
# a_function_requiring_decoration()
pass  # ---------装饰器的典型应用-----Logging 日志记录  2019-7-22 16:58:50
#
#
# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + " was called"
#             print(log_string)
#             # 打开logfile，并写入内容
#             with open(logfile, 'a') as opened_file:
#                 # 现在将日志打到指定的logfile
#                 opened_file.write(log_string + '\n')
#             return func(*args, **kwargs)
#
#         return wrapped_function
#
#     return logging_decorator
#
#
# @logit()
# def myfunc1():
#     pass
#
#
# myfunc1()
# # Output: myfunc1 was called
# # 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串
#
#
# @logit(logfile='func2.log')
# def myfunc2():
#     pass
#
#
# myfunc2()
# # Output: myfunc2 was called
# # 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
pass  # ----------装饰器的典型应用----授权  2019-7-22 16:58:50
# """对某些应用执行前做权限确认"""
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#     return decorated
pass  # ----------map,filter 内置函数-----------  2019-7-23 11:5:56
# print(list(filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5])))  # 筛选出条件为True的元素构成新列表
# print(list(n for n in [1, 2, 3, 4, 5] if n % 2))   # == 1 可缺省，True
# print(list(map(lambda x: x ** 2, [1, 2, 3, 4])))  # 对第一个元素作运算
# print(list(n ** 2 for n in [1, 2, 3, 4]))
pass  # ----------模块----------  2019-7-23 17:18:13
# print(sys.path)  # 系统搜索路径
# # 可通过sys.path.append() 添加，只在程序运行期间有效果
# sys.path.append('E:\\pydata\\HCNA-AI\\py-learning.git\\trunk\\OpenCv')
# print(sys.path)
pass  # ----------正则表达式----------2019-7-26 17:51:46
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配



if __name__ == '__main__':
    pass