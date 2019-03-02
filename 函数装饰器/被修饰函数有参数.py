def fa(func):
    print('exec fa()...')
    def f(a,b,z=10):
        print('>>>>>(a=%s,b=%s)' % (a,b))
        r = func(a,b)
        print('exec func() end , result=',r)
    return f

@fa
def add(a,b):
    return a+b

add(4,6)