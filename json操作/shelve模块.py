'''
shelve模块 比 pickle模块简单，只有一个open 函数，返回类似字典的的对象，用这个对象操作就是写入到文件
key 必须为字符串，而值无限制

这个和  dump方法区别在于，dump一次就必须将对象写完
如果想要加入写的对象，那么就必须重新读出来然后再加入新的对象然后再统一写进去,比较麻烦

但是 shelve 很方便的,因为读取出来的就是一个字典对象，可以直接现场同步操作
'''

import shelve

## 如下的命令首先要保证 目录 【shelve生成的文件】 是存在的
f = shelve.open('./shelve生成的文件/ff_shelve')
f['info']={'name':'qianyue','age':30}

## 可以看到总共会生成 3 个文件 .bak  .dat  .dir 3 个文件

f['append']={'schoole':'kejiadaxue'}

print(f.get('info'))