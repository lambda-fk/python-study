# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 19:33
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : linecache模块操作.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

'''
 linecache 模块允许 从python源文件中随机读取指定行，内部使用了缓存优化存储
 主要是用来读取  python 源文件的  使用的 utf-8 读取文件
   ##读取指定模块中指定文件的指定行。其中filename 指定文件名， lineno 指定行号。
   linecache.getline(filename, lineno, module_globals=None）：

  linecache.clearcache（）： 清空缓存

  ## 检查缓存是否有效。如果没有指定filename 参数，则默认检查所有缓存的数据。
  linecache.checkcache(filename=None）
'''
