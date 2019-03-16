'''
反射在很多语言中都有，Java中有，python中也有
而且 python 中反射的效率是比较高的
'''

class Stu:
    info = '类Stu的信息'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return '%s-%s ' %(self.name,self.age)

# 对象有一个 __dict__属性，该属性返回的是属性的字典
stu = Stu('qianyue',30)
print(stu.__dict__)
print(stu.__dict__['name'])

# 内置函数 getattr(对象，属性) , 属性的名字可以动态指定
print('内置函数getattr 方法使用...')
filed = input('输入 stu 属性名字:')
print(getattr(stu,filed))

# 内置函数 setattr 使用 , 动态添加属性
print('内置函数 setattr 使用 动态添加属性...')
setattr(stu,'height',170)
print(stu.height)

## 类也是对象，因此 getattr也可以用于类获取类的变量
print(getattr(Stu,'info'))

## 模块和函数也是对象，因此也是可以使用 getattr获取属性的值的，尤其是函数获取后是可以执行代码的

