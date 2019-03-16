# eval 函数 将字符串可以转换为对象
d = "{'a':1}"
v = eval(d)
print(type(v)) # <class 'dict'>
print(v) # {'a': 1}