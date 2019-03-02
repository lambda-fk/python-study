# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 20:19
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 迭代器.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

class MyIter:
    '''
      自定义一个迭代器
    '''

    def __init__(self,len):
        self.index = 0 ;
        self.__len = len

    def __next__(self):
        if self.__len == 0:
            raise StopIteration

        self.index += 1
        self.__len -= 1
        return self.index

    def __iter__(self):
        return self


it = MyIter(10)
print(next(it))

for x in it :
    print(x ,end='-')


