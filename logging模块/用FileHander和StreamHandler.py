import logging
'''
前面讲过这个使用 logging.basicConfig 进行日志输出的配置
这个函数里面的配置 属性中  filename 和 FileHandler对应
                          stream 和 StreamHandler对于
但是这样的配置有个缺陷 ， filename和 steam不能共存，有了 filename时候 stream就不起作用了
如果现在我们想 让日志既可以 输出到控制台也可以输出到文件
那么就可以使用  FileHandler 和 StreamHandler 来进行实现
'''

## 获取一个日志对象
logger = logging.getLogger()

## 创建一个 FileHandler
fh = logging.FileHandler('D:/Apl/log/handler.log')

## 创建一个控制台 StreamHandler , Stream
ch = logging.StreamHandler()

## 创建一个 Formmater
formatter = logging.Formatter('%(process)d %(thread)d %(funcName)s %(asctime)s %(filename)s [line:%(lineno)d] %(levelno)s %(levelname)s %(message)s')

## 将创建的 Formatter 对象传给  Handler （这个和配置参数的是对应的）
fh.setFormatter(formatter)
ch.setFormatter(formatter)

## 将创建的 Handler （FileHandler 和 StreamHandler ） 传给 logger 对象
logger.addHandler(fh)
logger.addHandler(ch)
## 明显这里使用了模式， 可以使用多个Handler来进行

logger.setLevel(logging.DEBUG)

## 这个时候 打印的日志是可以输出到 控制台或者文件
logger.debug(" 使用 logger来打印日志")
logger.info(" info 测试")
