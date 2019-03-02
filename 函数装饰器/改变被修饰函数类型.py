
def fa(func):
    return 'hello world '

@fa
def fb():
    print(' exec fb() ...')

print(type(fb))  # <class 'str'>
print(fb)  # hello world