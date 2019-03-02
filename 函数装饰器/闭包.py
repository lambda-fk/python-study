def outter(x):
    print('input: x= ',x)
    def inner():
        print('内部函数访问外部函数的变量 x= ',x)
        #x = 4  # 如果重新赋值的话就会产生变量遮蔽，重新定义了一个  x 那么上面的访问会出错
        ##########   UnboundLocalError: local variable 'x' referenced before assignment
    return inner

f = outter(2)
print('开始执行内部函数 inner 的代码体 ...')
f()