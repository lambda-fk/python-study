import pickle


## 将 pickle模块.py 中生成的函数的字节串拿过来 模拟另外一个程序接收数据
s = b'\x80\x03c__main__\nadd\nq\x00.'

## 为了使用 上面字节串定义的函数，需要重新定义这个函数
def add(x,y):
    return x+y

## 将字节串反序列化为 函数
f = pickle.loads(s)

print(type(f))
print(f(1,2,))

