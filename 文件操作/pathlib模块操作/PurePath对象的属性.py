'''
##-----------------属性介绍-----------------------
# PurePath.parts ： 该属性返回路径字符串中所包含的各部分。
# PurePath.drive ：该属性返回路径字符串中的驱动器盘符。
# PurePath.root ： 该属性返回路径字符串中的根路径
# PurePath.anchor ： 该属性返回路径字符串中的盘符和根路径
# PurePath.parents : 该属性返回当前路径 的全部父路径。
# PurePath.parent ： 该属性返回当前路径 的上 一级路径，相当于 parents[O］的返回值
# PurePath.name ： 该属性返回当前路径中的文件名。
# PurePath.suffixes ： 该属性返回当前路径中的文件所有后缀名。主要是针对文件名中有多个点情况
#PurePath.suffix ： 该属性返回当前路径中的文件后缀名。相当于 suffixes 属性返回的列表的最后一个元素。
# PurePath.stem ： 该属性返回当前路径中的主文件名 . 也就是去掉最后一个点剩下的文件名
# PurePath.as_posix（） ： 将当前路径转换成 UNIX 风格的路径 。
# PurePath.as_uri （）： 将当前路径转换成 URI。 只有绝对路径才能转换，否则将会引发 ValueError
# PurePath.is_absolute（） ： 判断当前路径是否为绝对路径
# PurePath.joinpath( *other）： 将多个路径庄接在一起
# PurePath.match(pattern） ： 判断当前路径是否匹配指定通配符。
# PurePath.relative to(*other）： 获取当前路径中去除基准路径之后的结果
# PurePath.with_name(name）： 将当前路径中的文件名替换成新文件名 如果当前路径中没有文件名，则会引发 YalueError
# PurePath.with_suffix(suffix）： 将当前路径中的文件后缀名替换成新的后缀名 。 如果当前路径中没有后缀名，则会添加新的后缀名
'''
print(__doc__)
from pathlib import *

## 访问drive 属性 , 只对 Windows下以 盘符开始的有用
print(PurePath('c:\\programs').drive) ## c:
print(PurePath('\programs').drive)  ## 空
print(PurePosixPath('/root').drive) ## 空

## 访问 root 属性 ， 对 Unix 下的开始目录有用，对windows 的以盘符开始的目录有用
print(PurePath('c:\\programs').root) ## \
print(PurePath('c:programs').root) ##  空
print(PurePath('\programs').root)  ## \
print(PurePosixPath('/root').root) ##  /

## 访问 anchor 属性 , 这个是带盘符的
print(PurePath('c:\\programs').anchor) ##  c:\
print(PurePath('c:programs').anchor) ##  c:
print(PurePosixPath('/root').anchor) ##  /

## 访问parents 属性
pp = PurePosixPath('/home','qianyue','data','python.py')
print(pp.parents[0])  ## /home/qianyue/data
print(pp.parents[1])  ## /home/qianyue
print(pp.parents[2])  ##  /home
print(pp.parents[3])  ## /
##print(pp.parents[4])  ## IndexError(idx)

## 访问parent 属性
print(pp.parent) ## 等价于 pp.parents[0]

## 访问 name 属性
print(pp.name) ## python.py
print(PurePath('/home','qianyue','data').name) ## data

## 访问 suffixes 属性
pp = PurePosixPath('/home','qianyue','data','20190216.log.bacup.tar.zip')
print(pp.suffixes) ## ['.log', '.bacup', '.tar', '.zip']
print(pp.suffix) ## .zip

## 访问stem 属性
print(pp.stem) ## 20190216.log.bacup.tar

## 风格转换
pp = PureWindowsPath('\home','qianyue','data')
print(pp.as_posix()) ##  /home/qianyue/data

## URI 转换 ，必须要绝对路径才可以
## print(PurePosixPath('home','qianyue','data').as_uri()) ## 报错 ValueError: relative path can't be expressed as a file URI
print(PurePosixPath('/home','qianyue','data').as_uri())  ## file:///home/qianyue/data
print(PurePosixPath('/home','qianyue','data','python.py').as_uri())  ## file:///home/qianyue/data/python.py

## 通配符
pp = PurePosixPath('/home','qianyue','data','python.py')
print(pp.match('*.py')) # True
print(pp.match('qianyue/*/*.py')) # True

## with_name 方法
print('原路径是:',pp)
print('study.py 替换后',pp.with_name('study.py')) ## study.py 替换后 /home/qianyue/data/study.py

## with_suffix方法替换后缀名
print(pp.with_suffix('.java')) ## /home/qianyue/data/python.java