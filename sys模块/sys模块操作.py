import sys

## sys.argv
## 获取 python 解释器的参数 ， 比如使用 python 命令执行的程序 传入参数
## 在命令行执行程序的时候 :   python  程序名  传入的参数列表
## 那么 上面对于 python解释器的 第一个参数 就是程序名 sys.argv[0]
## 因此我们的自定义参数是从 第二个参数开始的  sys.argv[1] 开始的

print('sys.argv 的类型是: ' , type(sys.argv)) # 是一个 列表
print(sys.argv) # ['D:/Apl/python/study/sys模块/sys模块操作.py']


## sys.exit(n)

##
print('python 解释器的版本 ',sys.version)

##  只是python的环境变量path
## 这个涉及到模块搜寻的路径的，因此我们命名的模块名字不能喝系统的模块名字重名
## 可以在计算机的 环境设置中 定义一个  PYTHONPATH 的变量名，这样自己写的模块可以放入到该目录下
#####这个在 控制台环境上我们的 模块就是可以被导入进来的
print('PYTHON 环境变量 :',sys.path)

## 平台名称
print(sys.platform) ## win32
import os
if sys.platform == 'win32':
    os.system('dir')
else :
    os.system('ls')


##标准输出
sys.stdout.write('please...')