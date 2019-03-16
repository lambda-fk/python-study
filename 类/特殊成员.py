
'''
类中存在一些特殊的方法，用于支持 python 的运行机制
也就是 python 中没有接口的显示实现，只要 python 类内部实现了规定的方法，那么
这个类就是实现了一个接口，不用像Java一样显示的实现接口
通过 实现 __XX__方法，该对象具有很多特性

'''
class Stu:
    def __init__(self,name):
        self.name = name

    ## 支持该对象使用内置函数 len()
    def __len__(self):
        print('实现了__len__，可以定义stu的长度')
        return 0

    ## 支持该对象为可迭代对象
    def __iter__(self):
        print('stu实现该方法可以成为可迭代对象...')
        return iter([4,5,6,7,8])

    ## 支持该对象使用 int() 函数
    def __int__(self):
        print('stu 可以使用 int()转换')
        return 0

    ## 支持该对象可以直接被 print 打印
    def __str__(self):
        print('stu被字符串...')
        return 'stu[name]:%s' % self.name

    ## 支持该对象可以执行函数代码体
    def __call__(self, *args, **kwargs):
        print('stu 可以执行代码体,参数是:',args)

    ## 支持该对象 使用 del 语句
    def __del__(self):
        print('调用stu的 del 方法')

    ## 支持该对象使用  [] 访问控制 , 并且支持切片
    ## 如果是 index 访问控制，那么 item 就是 int 类型或者是str 等基本类型的
    ## 如果是切片 ， 那么 item 就是 一  <class 'slice'> 的对象 类名就是 slice
    def __getitem__(self, item):
        if type(item) == slice:
            ## 切片操作
            print('切片操作...')
            print('起始位置:',item.start)
            print('终点位置:', item.stop)
            print('步长:', item.step)
            return 1
        else :
            print('索引位置操作...')
            print('可以支持对象stu 调用 st[%s] 操作...' % item)
            return item + 10


    ## 支持该对象使用 stu[100] = 101 形式操作
    def __setitem__(self, key, value):
        print('key=%s,value=%s' % (key,value))
        self.key = value

    ## 支持该对象 使用 del stu[100] 操作
    def __delitem__(self, key):
        print('删除指定的key')


# 1. 定义的 __init__方法 支持了构造函数调用
st = Stu('qianyue')

# 2. 定义的 __call__ 方法，那么该的对象就是一个可以被调用的，对象() 就会调用该方法的内部代码--可以认为实现了Call接口
st([1,2,3])
# 3. 定义的 __iter__ 方法，那么该对象就可以迭代的--可以认为实现了 Iter 接口
for s in st:
    print(s,end='-')

print()
# 4. 定义的 __len__ 方法，那么该对象可以使用 内置函数 len() 求长度，可以认为该对象是可求长的
len(st)
# 5. 定义的 __int__方法,那么该对象可以使用 内置函数  int() 进行类转换
int(st)
# 6. 定义的 __str__方法，那么外部可以使用 str() 作用该对象，因此可以直接使用 print() 打印
print(st)

# 7. 定义的 __getitem__ 方法，那么这个对象可以 使用[] 操作，类似列表一样的 例如 stu[1]
print(st[100])
st[2:3:6]
# 8.定义的 __setitem__ 方法，可以将对象如同列表一样 sut[100] = xx形式进行赋值的
st[101]='age'

## 还有其他很多的  __XX__ 类似的方法
del st