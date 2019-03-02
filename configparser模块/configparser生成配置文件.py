import configparser

config = configparser.ConfigParser()

## 设置配置文件中内容，采用字典方式设置
'''
例如我们要生成一个配置文件的内容为
[DEFAULT]
pagesize = 15

[jdbc]
url = http://127.0.0.1/mysql
user = qianye
password = 12345

[memory]
heap = 512
'''

## 生成的时候呀注意必须要满足上面的格式  [] 下面和他们的详细内容 ,而且值必须是字符串的
'''
使用 configparser 生成的 配置文件必须满足 下面的格式:

[seciton]
optinon=值

上面的格式称为一个  section
'''

## 注意生成方式的写法
config['jdbc'] = {'url':'http://127.0.0.1/mysql',
                  'user':'qianye',
                  'password':'12345'
                  }

## 注意如果要设置字典必须先要 创建出字典然后才可以使用  [][]进行赋值的
config['memory']={}
config['memory']['heap']='512'

config['DEFAULT']={}
default = config['DEFAULT']
default['pagesize']='15'

print('开始生成配置文件 sample.ini...')
with open('sample.ini','w') as configfile:
    config.write(configfile)

print('生成完毕')


