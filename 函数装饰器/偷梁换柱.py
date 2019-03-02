
def fa(func):
    print('exec fa()...')
    def f():
        print('exec f()...')
        print('===========')
    return f

@fa
def fb():
    print('exec fb()...')

fb()