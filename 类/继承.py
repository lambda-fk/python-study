
## 子类对象执行父类的方法时候，此时传入给父类方法中的self 就是当前方法调用对象

## 对于重新的方法，可以使用两种方式进行
###  super(子类，self).父类中方法()  或者  父类名.父类中方法(self,...)

## 多继承 方法探索路径，
# 左侧最先探索 , 一条路走到黑
## 如果有公共的根，根最后才执行

## 但是多继承体系中，任何使用了成员方法的地方都要遵循上面的规则，即使是 成员方法内部嵌套调用

## 多继承体系中，子类的创建，也只是找到第一个 __init__就可以执行

class BaseRequest:
    def __init__(self):
        print('BaseRequest.__init__执行')

class RequestHandle(BaseRequest):
    def __init__(self):
        ## 使用 父类.父类方法(self,...) 注意此时的 self不可以省略
        BaseRequest.__init__(self)
        print('RequestHandle.__init__执行')
    def server(self):
        print('RequestHandle.server()')
        self.request()

    def request(self):
        print('RequestHandle.request()')

class Minx:
    def request(self):
        print('Minx.request()')

class Client(Minx ,RequestHandle ):
    def __init__(self):
        super(Client,self).__init__()
        print('Client.__init__执行...')

client = Client()
client.server()