# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 0019 23:29
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : random模块.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

import random

## 0-1 之内的随机选择
print(random.random())  # 0-1 的随机数

## 范围之内的整数随机选择
print(random.randint(1,8)) ## 1-8 的随机数包括 8

## 常用的 randrange() 函数 ***** 是用率比较高
## randrange(n) : 表示 从 0- n-1 中随机抽取一个数字
## randrange(m,n) : 表示从 m - n-1 中随机抽取一个数字
print(random.randrange(1,6)) ## 生成1-5 之内的，不包含6 的随机一个数字
print(random.randrange(10))  ## 表示从 0-9 中任意选取一个数字

## 随机选择序列中的元素
print(random.choice('lambdafk')) ## 在序列中进行随机选择
print(random.choice([1,2,3,4,5])) ## 在列表中随机进行选择

###### 引申； random.choice() 方法可以随机在列表中选择数据

## 序列中随机选择指定的几个 组成新的一个序列 ， 例如下面的是 随机选择3个元素
print(random.sample([1,2,3,4,5],3))

## 打乱序列的顺序
#print(random.shuffle())

## chr() 函数可以将一个 数字 65-90 之间的转换成对应的 字母
print(chr(random.randrange(65,91)))  ## 表示从26 个字母中随机抽取一个



