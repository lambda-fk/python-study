import os

## 当前目录的绝对路径
print(os.path.abspath('.'))

## 路径分割,结果是一个元组 ， 纯粹的是最后一个 目录分隔符为界 分为两个部分(前面路径 ， 后面东西) 的一个元组
print(os.path.split(r'D:\python\python.exe'))  #  ('D:\\python', 'python.exe')
print(os.path.split(r'D:/Apl/python/study/os模块/path模块'))  #  ('D:/Apl/python/study/os模块', 'path模块')

## 获取一个文件的上层目录 , 不管是文件还是 目录，都是上层目录 , 就是 os.path.split 的第一个元素
print(os.path.dirname('D:/Apl/python/study/os模块/path模块/os.path模块操作.py')) #D:/Apl/python/study/os模块/path模块
print(os.path.dirname('D:/Apl/python/study/os模块/path模块')) #D:/Apl/python/study/os模块

## path的最后文件名，如果最后的path以这个 / 或 \ 结尾那么文件名就是空 ,如果不是就是 os.path.split 结果的第二个元素
print(r'D:\python\python.exe 的文件名是 :' , os.path.basename(r'D:\python\python.exe')) #python.exe
print(r'D:/python/ 的文件名是 :' , os.path.basename(r'D:/python/')) # 空
print(r'D:/python 的文件名是 :' , os.path.basename(r'D:/python')) # python


## 判断 path 是否存在
print(os.path.exists(r'D:\python\python.exe'))

## 判断 path 是否为绝对路径
print(os.path.isabs(r'D:\python\python.exe'))

## 判断path 是否为一个存在的文件
print(os.path.isfile(r'D:\python\python.exe'))
print(os.path.isfile(r'D:\python'))

## 判断path 是否为一个存在的 dir
print(os.path.isdir(r'D:\python'))


## **** 拼接路径 ， 但是这个方法只能拼接当前平台的字符串
## 对于 路径的拼接处理我们可以参照 pathlib 模块中的 PurePath 进行处理
print(os.path.join('/home','/user')) ## 返回的 /user
print(os.path.join('/','home','/user')) ## 返回的 /user
print(os.path.join('/','home','user')) ## 返回的是 /home\user
print(os.path.join('d:\\','user')) ## 返回的是 d:\user

