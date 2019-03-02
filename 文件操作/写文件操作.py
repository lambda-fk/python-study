# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 19:37
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 写文件操作.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

'''
1 文件指针 ： 用于标明文件读写的位置
    如果以  r+ , w, w+ 模式打开文件那么文件指针在文件开头处
    如果以  w+  或 w 打开文件 会清空文件
    如果以 a ,a+ 模式打开文件，文件指针在文件结尾处

2.操作文件指针
   文件对象提供了 seek 函数来移动文件指针

   seek(offset[,whence]): 将文件指针移动到指定位置处 ， offset表示移动几处
                          当 whence =0 ,   表示从文件开头开始计算,此时 offset指定的就是指针移动的地方
                          当whence = 1 ，表示从指针当前位置开始计算
                                    如 当前指针位置为 5 , offset =3 表示移动到文件的第 8 处
                          当 whence = 2, 表示从文件尾开始计算 ，
                                    如 offset = -3 表示移动到文件结尾倒数第3处
   tell() ： 判断文件指针的位置

   此外如果进行了文件数据的 读写 ，那么读写了多少个数据，文件指针自动向后移动多少个数据

 3.写文件的方法
   write(str或bytes) : 只有以 b 模式打开的文件才可以写入 字节串
   writelines(可迭代对象)


'''


