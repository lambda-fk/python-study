# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 18:53
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : fileinput模块操作.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

'''
 fileinput 模块提供的 input 函数可以把多个输入流合并在一起，一次性处理多个文件
    fileinput.input(files = None , inplace = False , backup = '' , bufsize=0,mode='r',openhook=None)
    其中的files 可以用于指定多个文件的输入流
    该函数返回一个 FileInput 对象 可以使用 for 循环来进行遍历
    该对象提供了如下的全局函数用于判断正在读取文件的信息
    fileinput.filename() : 当前正在读取的文件名称
    fileinput.fileno() : 返回当前文件的描述符 这是一个整数
    fileinput.lineno() : 当前正在读取的行号
    fileinput.filelineno(): 当当前读取的行在其文件中的行号
    fileinput.isfirstline(): 是否为第一行
    fileinput.isstdin():返回最后一行是否从 sys.stdin 读取， 可以使用 - 代表
    fileinput.nextfile(): 关闭当前文件开始读取下一个文件
    fileinput.close()
'''
