# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 17:07
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : fnmatch操作.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm

'''
前面介绍的文件操作的文件名称的 匹配都是很简单的
fnmatch 模块可以支持类似于 unix shell 风格的文件名匹配
* ， ？ ，[字符串序列]，[! 字符序列]
fnmatch.fnmatch(filename , pattern) 不区分大小写

fnmatch.fnmatchcase(filename , pattern) # 区分大小写

fnmatch.filter(names, pattern) # 对指定的 names列表中的元素进行 pattern 检查 符合的 元素输出到一个列表中
'''

import fnmatch
print(fnmatch.fnmatch('fnmatch操作.py','*操作.py'))  ## 不区分大小写 True
print(fnmatch.fnmatch('fnmatch操作.py','*操作.PY'))  ## 不区分大小写 True

print(fnmatch.fnmatchcase('fnmatch操作.py','*操作.py')) ## 区分大小写 True
print(fnmatch.fnmatchcase('fnmatch操作.py','*操作.PY')) ## 区分大小写 False

print(fnmatch.filter(['a.py','b.Py','c.PY','d.pY'], '*.py')) ## 对指定的 names列表元素检查 patter 不区分大小写
## ['a.py', 'b.Py', 'c.PY', 'd.pY']

## 将  unix shell 风格的 pattern 转换成一个 正则表达式
print(fnmatch.translate('*.py'))  ## (?s:.*\.py)\Z
