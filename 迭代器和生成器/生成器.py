# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 20:41
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 生成器.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

def addStep(x,step,maxValue):
    '''
    迭代器例子
    :param x: 基准值
    :param step: 步长
    :param maxValue: 最大值
    :return:
    '''
    print('函数执行...')
    cur = x
    cur += step
    print('yield cur')
    yield cur
    print('yield 3')
    yield 3
    print('yield 4')
    yield 4
    print('yield 5')
    yield 5
    return 'hello 生成器'

print('call addStep start...')
t = addStep(1,2,10)
print(type(t))
print('call next(t) ...')
print(next(t))
print(next(t))
print(next(t))
print(next(t))
#print(next(t))

