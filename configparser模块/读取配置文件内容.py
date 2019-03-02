import configparser

'''
读取配置文件信息
注意这个 读取的时候都要从这个 config 开始进行读取
不用从中间的 sections那里使用连环的对象调用
'''

config = configparser.ConfigParser()
config.read('sample.ini',encoding='utf-8')

## 用这个 sections() 读取的时候注意 DEFAULT 的块是读取不出来的
print(config.sections())
for s in config.sections():
    print('[',s,']')
    for op in config.options(s): ## 读取一个块中的 options ， 注意此时 default中的op 是可以被读取出来的
        print(op,'=' ,config.get(s,op))
    print()

## 读取 default块
print(config.default_section)
## 读取 default块中内容

print('\n是否含义 section -jdbc')
print(config.has_section('jdbc'))

print('是否含义 option-')
print(config.has_option('add','test'))