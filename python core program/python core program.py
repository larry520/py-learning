#-*- encoding: utf-8 -*-

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

import  numpy as np
import copy
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
pass # ---------复数 i 用 j 或 J 来表示
# # num.real 该复数的实部  浮点类型
# # num num.imag  该复数的虚部  浮点类型
# # num.conjugate() 返回该复数的共轭复数
# a = 2 + 3j
# b = 3
# c = a +b
# print(c, c.real, c.imag, c.conjugate())
pass # ---------深拷贝copy.deepcopy()与浅拷贝.copy [:]
alist = [1,  ['a', 'b']]
blist = alist    # 引用,指向同一个list
clist = alist[:]   # 浅拷贝
# 浅拷贝  作用同 blist = alist.copy()
# 对于列表中的元素为容器情形只拷贝容器地址
dlist = copy.deepcopy(alist)   # 深拷贝
print(alist,blist,clist,dlist)
alist[0] = 'wa'
alist[1][1] = 'c'
print(alist,blist,clist,dlist)








if __name__ == '__main__':
    print('test module')
