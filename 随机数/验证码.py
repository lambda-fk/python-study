# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 0020 0:02
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 验证码.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

import random
def vcode(n):
    '''
    生成随机的 n 位 验证码
    :param n: 验证码的位数
    :return:
    '''
    v = ''
    ##验证码由这个数字和字母随机组合  ，因此每次要从数字和字母之间选取一个，总共有 n 位

    for i in range(n): # 生成从 0-n-1 共有 n 个数
        d_a = random.choice([random.randrange(10) , chr(random.randrange(65,91))])
        v+= str(d_a)

    return v

print(vcode(6))

