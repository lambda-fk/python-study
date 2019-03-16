'''
python 中一切都是对象： 模块 ， 函数 ， 类也是一个对象
（类是 type的对象）
通过 type 来创建类
类的本质1： 类是type的对象
'''
print('通过 type来创建一个类...')
## 通过type创建一个类，当然类的成员定义要先准备好
# 其中指定的 self 是和当前的调用对象进行绑定的
def setname(self,name):
    self.name = name

Stu = type('Stu',(object,),{'setname':setname,'show':lambda self:print(self.name)})
st = Stu()
st.setname('qianyue')
st.show()

## 默认情况下我们创建的类 都是使用 type 创建的，包括我们自己定义的类


## 使用自定义的 type 子类创建我们的类  ，需要使用 metaclass
## 一旦使用了 metaclass 之后，那么当我们自己定义类的时候，就会先调用  我们自定义的type
## 注意时点是： 类的创建
class MyType(type):
    def __init__(self,*args,**kwargs):
        print('使用自定义的type')

class A(metaclass=MyType):
    pass


'''
类的本质2：
我们知道一个 对象 obj , 如果对象使用了 obj(),那么表示了该对象实现了 __call__方法
那么 ，类本身也是一个对象，对于一个类 Stu , 如果使用构造函数 Stu()
这个道理其实呢 和 obj也是一样的，所以 Stu这个类，也是对象，当执行的构造函数本质
上是 Stu本身也有 __call__, 然而 类 是 type的对象，所以
调用类的构造函数其实呢是执行了 type的__call__
因此执行类的构造函数时候，首先要先执行 type的 __call__
然后 这个__call__里面会先调用 被创建类的 __new__方法,这个__new__方法是类的,第一个参数是cls
__new__方法才是真正创建对象的地方
调用完 __new__之后创建了obj,才会调用 __init__方法
'''

print('类创建的过程解析...')
class MyType(type):
    ## 注意 MyType中的 self就是 被创建的类这个对象
    def __init__(self,*args,**kwargs):
        print('使用自定义的type')
    def __call__(self, *args, **kwargs):
        print('使用构造函数时候其实执行的 type的 __call__方法')
        ## 此时的 self 就是当前被创建的类，在该例子中就是 类A
        obj = self.__new__(self,*args,**kwargs)
        ## 此时才会调用这个 init 方法，之所以类中方法第一个参数绑定当前对象就是此处将创建的对象传入进去了
        self.__init__(obj)


class A(metaclass=MyType):
    def __init__(self):
        print('创建对象A ')

    ## 注意这个方法是 cls,是类的绑定
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls,*args,**kwargs)

a = A()