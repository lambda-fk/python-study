# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 22:03
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 生产者消费者模型.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm


global i
i = 0

def creator(tables=[]):
    '''
    生产者
    :param tables:
    :return:
    '''
    print('生产者开始工作...')

    while len(tables) == 0 :
        print('没有蛋糕了要开始做...')
        tables.extend(['A_'+str(i),'B_'+str(i)])
        print('已经做好了两个蛋糕...')
        print('可以吃蛋糕了...')
        yield tables
        tables.clear()


def consumer(gg):
    '''
      消费者
    :param gg:
    :return:
    '''
    print('吃了蛋糕 ( ',next(gg) , ')')
    print('蛋糕吃完了')

gg = creator([])
while True:
    i = i+1
    consumer(gg)