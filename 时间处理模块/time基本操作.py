# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 0019 22:42
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : time基本操作.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

import time

## 提供操作时间值的模块
## 表达时间 的方式 -1  时间戳： 从unix 诞生的1970 年到现在经历了多少秒
print(time.time()) # 计算1970 到现在的多少秒  1550587571.8147445  ******

# 这个只是 计算 cpu 的执行时间 ， 但是代码中 的 time.sleep() 的时间一般是不计算的
print(time.clock())

## 迟延 3 秒   *****
time.sleep(3)

## UTC : 时区
print(time.gmtime())
## 结构化时间 time.struct_time(tm_year=2019, tm_mon=2, tm_mday=19, tm_hour=14, tm_min=54, tm_sec=23, tm_wday=1, tm_yday=50, tm_isdst=0)
## 注意了这个时间 tm_hour , UTC时间是英国所在的格林尼治台中心的时间 ，因为中国为东8区，所以这个时间和 当前系统时间差了 8 个小时
## 其中的tm_wday=1, tm_yday=50  表示 每周的第几天 和 每年的第几天

## 时间表示2  本地时间  ********* ,获取当前计算机时间
print(time.localtime())
##time.struct_time(tm_year=2019, tm_mon=2, tm_mday=19, tm_hour=23, tm_min=2, tm_sec=27, tm_wday=1, tm_yday=50, tm_isdst=0)

##时间表示3  strftime : 表示字符串格式化的时间  str  fomrat简写的f  time , 表示格式化时间为字符串
##print(time.strftime())
'''
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
'''
## 这里的 p_tuple 可以使用 结构化时间充当
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))


## strptime : 将字符串表示的时间格式化为元组的形式,也就是格式化的时间
s_time = time.strptime('2019-02-19 23:12:28','%Y-%m-%d %H:%M:%S')
print(type(s_time))  ## <class 'time.struct_time'>
## 注意 这个 struct_time 就是一个元组
print('年为：',s_time.tm_year)


## ctime()
print(time.ctime())  ## Tue Feb 19 23:20:49 2019

## 将结构化时间转换成时间戳
print(time.mktime(time.localtime()))

