import logging

## 日志的级别从  低到高 ， 默认情况下 只从 waring 之后的级别开始,debug和info 是不打印的
#logging.debug(msg , *args , **kwargs)
'''
logging.debug('debug msg')
#logging.info(msg , *args , **kwargs)
logging.info("info msg")
logging.warning("warning msg")
logging.error("error msg")
logging.critical("critical msg")

## 灵活配置日志  
## kwargs : 表示的是关键字参数
## 属性有 filename: 用指定的文件名创建 FileHandler,指定日志输出的文件,因此可以使用文件或者FileHandler
##        filemode: 文件打开方式
##        datefmt: 日志的格式
##        level：日志级别
##        stream: 用指定的stream创建 StreamHandler . 例如 sys.stderr 和 sys.stdout 。同时有filename 和 steam 时候 ， stream会被忽略掉7
##        fromat: 指定handler 使用的日志格式显示
## 注意这个 format 关键字参数 ， %(变量名)
## 其中的 format 关键字中变量有如下可设置变量:
#        %(name)s 就是 Logger的名字
#        %(filename)s 就是调用日志输出函数的模块的文件名 , 
#        %(levelname)s 就是关键字参数 level对应的文本形式
#        %(levelno)s 就是当前日志级别的数字形式
#        %(pathname)s 调用日志输出函数的模块的完整路径名
#        %(module)s  调用日志输出函数的模块名
#        %(funcName)s 调用日志输出函数的函数名
#        %(lineno)d  调用日志输出函数的语句所在代码行 数字
#        %(message)s 就是我们 日志要打印的message
#        %(created)f 当前时间用 UNIX 标准的表示时间的浮点数
#        %(asctime)s 字符串形式的当前时间
#        %(thread)d  线程id
#        %(threadName)s 线程名
#        %(process)d 进程id

logging.basicConfig(level=logging.DEBUG, ## 设置日志级别
                    format = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s' ,## %() 中的都是变量，下面会有定义
                    datefmt = '%a ,%d %b %Y %H:%M:%S',
                    filename = 'D:/Apl/log/debug.log', # 可省略
                    filemode = 'w' ## 注意这个写文件模式为w 写入 ，可省略
                    )
'''

#输出 debug和info 的日志
logging.basicConfig(level=logging.DEBUG)
logging.debug(" debug message is can log ")
logging.info(" info message is can log")

