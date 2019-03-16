'''
类的内部成员 如果使用 __开头进行命名的，那么类的外部是无法直接访问的
而且 对于__定义的私有字段，那么对于继承，子类也是无法获取到的

@staticmethod 可以定义静态方法
'''

class Stu:
    info='静态字段'
    __info='被隐藏的静态字段'
    '''
    定义类的静态方法 使用 @staticmethod 修饰
    '''
    @staticmethod
    def getinfo():
        return Stu.__info
    def __init__(self,name,age):
        self.name = name
        self.__age = age # 通过 __命名方式进行隐藏
    def getage(self):
        return self.__age
    def __private(self):
        print('私有的private方法无法再外部直接使用')
st = Stu('qianyue',30)
print(Stu.info)
print(Stu.getinfo())
#print(st.__age) # AttributeError: 'Stu' object has no attribute '__age'
print(st.getage())



