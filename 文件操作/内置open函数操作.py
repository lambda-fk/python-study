# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 17:19
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : 内置open函数操作.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

'''
 open 函数是一个内置的函数 ， 用于打开文件
   open(file_name,[,access_mode],[,buffering])
           ## 注意了open 函数打开文件默认使用 当前os 的编码
           ##  windows 平台就是 gbk ,因此如果在该平台下打开一个文件有汉字情况再读取时候会有
           ##   UnicodeDecodeError 异常的
           ##  所以使用 open 函数在 windows 平台打开文件时候需要对读取的内容进行译码的 ， 有两种方式

   打开模式分为：
   ------------------------
   模式                意义
   ------------------------
     r              只读模式 ( 只有这种方式的时候，要求打开的文件必须存在 ，r+ 也是)
     w              写模式 （只用这种方式打开文件会清空原有内容 w+ 也是的）
     a               追加模式
     +               读写模式可与其他模式结合 比如 r+ 和 w+ 都代表  读写模式
     b               二进制模式  （用于打开音频图片等文件）
     ===============================

     缓冲
     第三个参数 为  0 或者 False : 表示没有缓冲
     第三个参数为   1 或者 True : 存在缓冲
     第三个参数为 > 1 的整数： 表示缓冲区大小
     第三个参数为 负数： 缓冲区使用默认大小

'''


## 文件对象的 read 方法可以按照字节或字符来读取文件，取决于文件打开的模式
## 调用 read 时候可以传入一个 参数 表示一次读取  几个字符或者 几个字节 ， 如果不传入表示全部读取

f = open('ntpath的属性.property','r',True)
while True:
    ch = f.read(1)
    if not ch : break  ## 读到文件末尾
    print(ch,end=' ')  ## 每次一个字符读取输出
f.close()

## read 方法一次全部读取
f = open('ntpath的属性.property','r',True)
while True:
    ch = f.read()  ## 没有传入参数
    if not ch: break
    print(ch)
f.close()

## 打开文件编码的问题，open函数使用os 的编码打开文件，因此windows 下打开一个汉字文件是用的gbk
## 因此需要进行 译码的操作 有两种方式可以进行
## 译码方式1： 使用 b 模式打卡，这样可以使用 bytes 对象的 decode 方法了
print('\n 使用 open 函数打开文件加上b 模式，这样可以使用 bytes 对象的decode 方法进行译码')
f = open('fnmatch操作.py','rb',True)  ## 必须传入 b 模式，不然是没有 decode 方法的
while True:
    ch = f.read().decode('utf-8') ## 如果不加译码就会报错的
    if not ch: break
    print(ch)
f.close()

## 译码方式2 ； 使用 codecs 模块的 open 函数来打开文件，此时可以指定 字符集
print('\n使用 codecs 模块的 open 函数打开文件指定字符集解决译码问题...')
import codecs

f = codecs.open('fnmatch操作.py','r','utf-8',buffering = True)
while True:
    ch = f.read()
    if not ch: break
    print(ch)
f.close()


## 按照行来读取
## readline([n]) : 如果指定 n 那么就读取此行内的 n 个字符，不指定就是读取一行
## readlines() : 读取所有行

