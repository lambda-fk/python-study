'''带有输入参数的函数装饰器'''
import os
def log(isFout=False):
    def fa(func):
        print('exec fa()...')
        def f(*args):
            print('>>>>>(a=%s,b=%s)' % (args[0], args[1]))
            r = func(args[0], args[1])
            if isFout:
                f = open('add.log','a')
                print('计算 %s + %s 的值, 结果= %s' % (args[0], args[1],r) ,file=f)
                print('计算结果已经输出到文件 %s\\add.log 中了 ' % os.getcwd())
                f.close()
            else:
                print('计算 %s + %s 的值, 结果= %s' % (args[0], args[1], r))
        return f
    return fa

@log()
def add(x,y):
    return x + y

@log(True)
def add1(x,y):
    return x + y

print('add(2,3)...')
add(2,3)
print('add(5,7)...')
add1(5,7)