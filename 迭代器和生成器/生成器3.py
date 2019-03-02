# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 21:47
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 生成器3.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

def addStep(x,step,maxValue):
    param = None
    while x < maxValue:
        param = (yield param + step + 1) if param is not None else (yield x+step)
        if param is not None:
            print('yield 传入的值是 :',param)

g = addStep(1,2,40)
print('开始进行生成...')
print(g.send(None))
print('调用 send(8)...')
print(g.send(8))

print('调用 send(10)...')
print(g.send(10))
