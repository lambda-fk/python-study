class Sigleton:
    ## 静态类属性
    __instance = None

    ## 定义一个类方法
    @classmethod
    def getInstance(cls):
        if cls.__instance:
            return cls.__instance
        else :
            cls.__instance = Sigleton()
            return cls.__instance

    def __init__(self):
        pass


obj = Sigleton.getInstance()
print(obj)
obj1 = Sigleton.getInstance()
print(obj1)
obj2 = Sigleton()
print(obj2)