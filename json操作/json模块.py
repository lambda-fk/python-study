'''
json 可以将普通的对象转换为字符串
但是对于 高级的对象如 函数，类是无法进行转换的这点要注意
对于 字典 ， 列表 ， 元组 等都是可以的
json 是一个 json 序列化类型的

如果想支持更多的可以使用 pickle进行 ， 但是这个只能在 python 内进行
此时可以将这些对象转换为 字节串
'''
import json

stu = {'name':'qianyue','age':30}
# 将stu 进行序列化 dumps 方法
s = json.dumps(stu)
print(type(s)) # <class 'str'>
## 说明 json 序列化的结果是一个字符串
print(s) # {"name": "qianyue", "age": 30}

# 反序列化  loads方法
data = json.loads(s) # <class 'dict'>
print(type(data))
print(data)

## dump 方法 和 dumps方法区别
'''
使用 dump 方法呢和 dumps有一些区别，
该方法时候可以指定文件句柄将对象序列化之后直接写入到文件中
而 dumps 中没有文件句柄的

下面是 dump 方法定义
dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw)
'''


'''
load 和 dump是对应的 ， 因此 load也可以接收到一个文件句柄然后加载其中内容反序列化
load(fp, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

如果要讲 json 写入文件 和从文件中读取的时候，那么使用  dump 和 load 方法是便捷的
'''
