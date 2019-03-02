# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 21:10
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 生成器2.py
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
    while (cur+step) <= maxValue:
        cur += step
        yield cur

print('call addStep start...')
t = addStep(1,3,10)
print(type(t))
for x in t:
    print(x,end='-')