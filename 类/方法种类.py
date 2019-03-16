
class A:
    def __init__(self):
        pass

    ## 类的成员方法
    def show(self):
        print('show 执行')

    ## 静态方法 , self 就不是必须的参数了 , 由类之间调用
    @staticmethod
    def staticMethod(a,b):
        return a+b

    ## 类方法 , 传入进去的参数是 cls ,描述的是类的信息
    ## 静态方法和使用类方法是类似的
    @classmethod
    def classMethod(cls):
        pass
