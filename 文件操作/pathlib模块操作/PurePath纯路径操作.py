'''
PurePath 表示一个纯路径操作的类，也就是只操作路径字符串
有两个子类， PurePosixPath  和 PureWindowsPath
他们包装的路径就是 文本字符串
'''

from pathlib import *

pp = PurePath('add.log')
print(type(pp))  ## <class 'pathlib.PureWindowsPath'>

## 默认使用当前系统的风格创建目录 , 可以只传入各个目录的名字即可进行连接
pp = PurePath('sys','python','user')
print(pp)   ## sys\python\user

## 使用 Path对象 来构建 PurePath 对象
pp = PurePath(Path('c:\\'),Path('programs'))
print(pp)  ## c:\programs

## unix 风格的目录路径
pp = PurePosixPath('home','qianyue','data')
print(pp)  ##  home/qianyue/data

## 不传入参数默认使用当前的目录 .
pp = PurePath()
print(pp)  ## .

## 如果传入是多个 根目录开始，则最后一个生效
pp = PurePosixPath('/root','/home','/user/application')
print(pp)  ##  /user/application

pp = PureWindowsPath('c:\\','d:\\')
print(pp)  ## d:\

## PurePath 处理多余的斜杆和点号  (在 路径分隔符之间的，如果跟着目录名则认为是目录名一部分)
pp = PurePosixPath('//home./qianyue//./application')
print(pp)  ##  //home./qianyue/application

print(PurePosixPath('info') == PurePosixPath('INFO'))  ##  False

print(PureWindowsPath('info') == PureWindowsPath('INFO')) ## True

## 字符串比较大小

##  UNIX 风格区分大小写，因此 'D:' <  'c:'
print(PurePosixPath('D;') < PurePosixPath('c:'))  ## True

## windows 风格不区分大小写 所以  d: 和 D: 是一样的 ，所以 d: > c:
print(PureWindowsPath('d:') > PureWindowsPath('c:'))  ## True

## 不同风格的路径字符串可以判断是相等 ， 但是不能比较大小
print(PurePosixPath('info') == PureWindowsPath('info')) ## False

## print(PurePosixPath('info') > PureWindowsPath('info'))  ## 不能比较大小，不然报错
## TypeError: '>' not supported between instances of 'PurePosixPath' and 'PureWindowsPath'

## PurePath 支持斜杠  /  作为路径运算符（重载过）
pp = PurePath('qianyue')
print(pp / 'python' / 'study') ##  qianyue\python\study

## PurePath 支持 两个 PurePath 对象使用 斜杠  /  进行路径的拼接
pp1 = PurePosixPath('/home')
pp2 = PurePosixPath('qianyue','data')

print(pp1 / pp2)  ## /home/qianyue/data

## 可以使用  str() 函数将 PurePath 对象恢复成 字符串对象
print(str(pp1 / pp2))
