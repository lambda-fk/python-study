# coding = UTF-8
def fa(func):
    print('exec fa()...')
    def f(*args):
        print('>>>>>(a=%s,b=%s)' % (args[0],args[1]))
        r = func(args[0],args[1])
        print('exec func() end , result=',r)
    return f

@fa
def add(a,b):
    return a+b

add(4,6)
print('函数装饰器')
