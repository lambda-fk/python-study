'''
os模块的path 也可以进行操作
'''

import os
import lambdafk.util as util
import time
#输出 os 模块的属性 , 这个借助之前封装的功能
util.outAttr2f(os.path)

## 获取绝对路径 os.path.abspath
print(os.path.abspath('os.path操作.py')) ## D:\Apl\python\study\文件操作\os.path操作.py

## 获取路径的共同前缀名 os.path.commonprefix
print(os.path.commonprefix(['/home/qianyue/data','/home/quick']))  ## /home/q

## 获取文件的目录 os.path.dirname
print(os.path.dirname('D:\Apl\python\study\文件操作\os.path操作.py'))

## 判断指定目录是否存在
print(os.path.exists('D:\Apl\python\study\文件操作'))

## 获取文件最近一次访问时间  get_access_time 的缩写  getatime
print(os.path.getatime('os.path操作.py'))  ## 1550394003.8790202
print(time.ctime(os.path.getatime('os.path操作.py')))  ## Sun Feb 17 17:05:47 2019

## 获取文件最后一次修改时间 getmtime
print(time.ctime(os.path.getmtime('os.path操作.py')))

## 获取文件的创建时间
print(time.ctime(os.path.getctime('os.path操作.py')))

## 获取文件大小
print(os.path.getsize('os.path操作.py')) ## 1401

## 判断文件是否为目录
print(os.path.isdir('os.path操作.py'))
print(os.path.isfile('os.path操作.py'))

## 判断是否为同一个文件
print(os.path.samefile('os.path操作.py','./os.path操作.py'))

