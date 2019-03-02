import os

## 当前工作目录
print(os.getcwd())  ## 绝对路径  D:\Apl\python\study\常用模块\os模块

## 当前路径
print(os.curdir)  ## 这是一个属性不是方法 ， 返回的是一个点

print(os.pardir) ## 属性表示 父亲目录 两个点

## 生成多个目录，按照路径中的多个 目录名生成
## os.makedirs(路径 ， mode , )  如果目录中有子目录的话，就会递归生成
## 路径如果不是绝对路径，那么就表示从当前路径开始 创建文件夹

## 只生成一个目录
#os.mkdir()

## 更改路径
# os.chdir(路径)

## 删除多个目录，根据指定的路径中的 多个目录进行删除
## os.removedirs(路径) : 这个删除必须要保证 目录下面没有文件才会进行删除的 ， 如果不为空则不能删除
   ## 只能删除空文件夹


## 只能删除文件，不能删除目录
#os.remove()

## 获取指定路径的所有目录和文件夹, 返回的结果是 列表
print(os.listdir('d:/'))

## 重命名
#os.rename(src,dist)  重命名文件夹
#os.renames(old,new)  重命名文件名

## 操作系统的指定分隔符
print(os.sep)

## 查看目录状态信息
print(os.stat(r'd:\python')) ## 结构化信息 os.stat_result , 也是一个元组信息，重要的是 文件大小 size
r = os.stat(r'.\os模块基本操作.py')
print('文件的大小是:',r.st_size)

print(os.linesep)  ## 当前平台的行终止符  Windows下是 \r\n  , linux 下是\n ,mac是 \r

## 执行shell命令
os.system("dir")

## 获取环境变量
os.environ  ## 这是一个字典





