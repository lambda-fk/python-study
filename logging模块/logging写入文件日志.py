import logging


logging.basicConfig(level=logging.DEBUG, ## 设置日志级别
                    format = '%(process)d %(thread)d %(funcName)s %(asctime)s %(filename)s [line:%(lineno)d] %(levelno)s %(levelname)s %(message)s' ,## %() 中的都是变量，下面会有定义
                    datefmt = '%a ,%d %b %Y %H:%M:%S',
                    filename = 'D:/Apl/log/debug.log', # 可省略
                    filemode = 'a' ## 注意这个写文件模式为w 写入 ，可省略
                    )

def logTest():
    logging.debug(' logging 写入文件日志')
    logging.info('输出完毕')

logTest()
