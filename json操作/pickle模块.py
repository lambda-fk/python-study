'''
使用 pickle 的操作可以如同 java一样将函数或者类的对象保存于文件中
但是这个操作只能局限于 python 内部

'''
import pickle

def add(x,y):
    return x+y

data = pickle.dumps(add)
print(type(data)) # <class 'bytes'>  说明结果是一个 字节串
## 如果使用文件写入的时候 ， 注意文件的打开模式要带有 b 模式的
print(data) # b'\x80\x03c__main__\nadd\nq\x00.'

ff = pickle.loads(data)
print(type(ff)) # <class 'function'>
print(ff(2,3))

## 需要注意的问题，如果我们将一个函数存于这个文件中的时候
## 然后另外一个程序读取这个文件将这个函数读取出来之后可要注意了
## 读取出来的函数无法使用了，因为没有对应的内存地址了，如果需要使用需要 在使用方定义相同的函数才可以的
## 因为读取出来的函数只有函数名字啥信息的