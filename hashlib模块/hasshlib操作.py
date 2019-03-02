import hashlib

## 可以用于加密 md5 和 sha

m5 = hashlib.md5()
print(type(m5)) ## <class '_hashlib.HASH'>
print(m5)

## 加密
m5.update('hello world'.encode(encoding='utf-8'))  # # 返回值为 None
## 必须要进行逐个 译码， 因为 m5.updat（） 要接受一个 bytes 数据的 ， 必须要通过 encode 来进行 转换
## 不然会有 TypeError: Unicode-objects must be encoded before hashing

print(m5.hexdigest()) ## 加密的东西 5eb63bbbe01eeed093cb22bb8f5acdc3

## 第二次继续加密
m5.update('python'.encode(encoding = 'utf-8'))
print(m5.hexdigest()) ## 加密的东西 5644d5b4bbb70375817025a5a03c810c

## 那么上面两次加密的关系是什么呢
## 其实就是 等价于 将上面的 hello world和python 拼接之后进行一个加密
m2 = hashlib.md5()
m2.update('hello worldpython'.encode(encoding = 'utf=8'))
print(m2.hexdigest()) ## 5644d5b4bbb70375817025a5a03c810c

## 所以连续调用 update 的效果就是把字符串拼接起来然后统一进行一个 encode 然后获取一个 hexdigest()

'''
  使用的这些加密 都是不可逆的
'''
print('\n 使用 sha1 加密 helloworld.............')
s1 = hashlib.sha1()
s1.update('helloworld'.encode(encoding='utf-8'))
print(s1.hexdigest())

print('\n 使用 sha256 加密 helloworld.............')
s2 = hashlib.sha256()
s2.update('helloworld'.encode(encoding='utf-8'))
print(s2.hexdigest())


