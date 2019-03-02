'''
##-----------Path 功能用法
# Path是真正操作操作系统的类
# 也提供了  PosixPath  和  WindowsPath 两个子类
# 通过path 可以操作真正的文件
# path对象提供了很多 is_xxx() 方法用于判断 该path 对应的路径是否为 xxx
[is_absolute,is_block_device,is_char_device,is_dir,is_fifo,is_file,is_mount,is_reserved,is_socket,is_symlink]
iterdir
joinpath
match
mkdir
name
open
glob

注意： Path 也重载了 / ，因此可以使用两个 Path 对象进行这个 / 的操作
       但是这样会 将两个目录 按照 路径组成 父子关系
         p = Path(__name__) / Path('data.txt')
         输出为 __main__\data.txt

'''

from pathlib import *
## 将Path 的属性输出到文件 Path的属性.proper 中
p = Path('Path的属性.proper')
if not p.exists():
    print('将Path的属性读入到文件: ',p.name)
    f = open('Path的属性.proper','a')
    print(dir(Path),file=f)
    for p in dir(Path):
        print(p,file=f)
    f.close()

## 上面这段代码我们可以封装起来做成公用的模块 , 参照包 lambdafk 下的uitl.py

## 获取当前目录
p = Path('.')
## 遍历当前目录下所有的文件和子目录
print('-----------Path的 iterdir() 方法使用-------')
for x in p.iterdir():
    print(x)

print('-----------Path的 glob() 方法使用-------')
## 获取上一级目录
p = Path('../')
## 获取该目录下面的所有 py 文件
for x in p.glob('**/*.py'):
    print(x)


## Path 来读取文件 和写文件
## 使用 Path('文件路径') 就可以打开一个文件了

print('-----------Path的 read_text() 方法使用-------')
p = Path('Path的属性.proper')
content = p.read_text(encoding = 'utf-8')
print(content)

print('-----------Path的 read_bytes() 方法使用-------')
b = p.read_bytes()
print(b)

## 使用Path 创建目录的方法，先用这个Path 构建一个目录对象，然后调用 path 对象的 mkdir 就用给定的path创建一个目录
## 调用 mkdir 的时候 有两个默认参数注意下： 一个是 mode,一个是是否为父目录默认为 False，表示子目录
print('-----------Path的 mkdir() 方法使用-------')
p = Path('./filedata')
if not p.exists():
    p.mkdir()
    p.chmod(777)

## 使用 Path 对象重载的 / 运算符 构建一个Path 对象
p = p / Path('text.txt')   ## 注意打开的时候没有指定 是追加还是什么的方式
## 注意这种写入 会覆盖掉原先的内容
cnt = p.write_text('使用 path 的 write_text 方法写入了 hello world ',encoding = 'utf-8')
print('p.write_text() 一共写入了 %s 个字符'% cnt)

## bytes 可以使用 b+ ASC码 进行构建
bdata = b'hello python'
cnt = p.write_bytes(bdata)
print('p.write_bytes() 一共写入了 %s 个字节'% cnt)

## 可以使用 bytes类构造函数创建一个bytes 对象
bdata = bytes('使用 btyes 书写 的内容',encoding='utf-8')
cnt = p.write_bytes(bdata)
print('p.write_bytes() 一共写入了 %s 个字节'% cnt)

##使用字符串的  encode 构建一个 bytes 对象
bdata = '正在学习Path 类的用法 , 构建一个 bytes 对象'.encode(encoding = 'utf=8')
cnt = p.write_bytes(bdata)
print('p.write_bytes() 一共写入了 %s 个字节'% cnt)

print('写入完毕!')
print('读取文件 text.txt 最终的内容是: ')
content = p.read_text(encoding='utf-8')
print(content)


