# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 19:09
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 文件迭代器.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

'''
 文件对象本身就是可以遍历的， 因此可以使用 for 循环来 遍历 文件对象
 所以这个 文件对象也是一个可迭代的东西，可以使用 list() 将文件对象转成 列表

 sys.stdin 也是一个类文件对象 ， Python中的很多IO 都是文件对象

'''

import codecs
f = codecs.open('fileinput模块操作.py',mode='r' , encoding = 'utf-8')

ll = list(f)  ##一旦使用 list() 函数等将文件对象转换成 列表，那么这个文件对象是被迭代完了的后面无法再使用f 了
print('文件对象被转成的 列表内容:','\n',ll)

## 文件对象充当一个函数迭代器
for line in f:
    print(line)
f.close()


## sys.stdin 获取用户的输入,用户输入什么就返回什么
import sys
for line in sys.stdin:
    print('用户的输入是 :',line ,end=' ')


