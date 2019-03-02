'''
使用元组做一个生成器
元组 进行的 for 推倒就是一个生成器
这个和列表的 for 推导式是不同的
'''

def func(x):
    return x**2

l = [1,2,3,4,5]
print('列表 l=',l)
ftl = [func(x) for x in l]
print('列表l 的 for 推导式类型是:',type(ftl))
print('列表生成器得到的列表是：',ftl)

t = (6,7,8,9,10)
print('元组 t=',t)
ftt = (func(x) for x in t)
print('元组t 的 for 推导式类型是:',type(ftt))
print('调用生成器的 next 函数:',next(ftt))

print('剩下的生成器元素是:')
for x in ftt:
    print(x,end=',')


