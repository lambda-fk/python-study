# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 0016 23:37
# @Author  : 千月
# @Email   : fk216@126.com
# @File    : util.py
# @Blog    ：https://blog.csdn.net/fk002008/article
# @Software: PyCharm


from pathlib import Path,PurePath

'''
工具模块

'''
def outAttr2f(module , recreate = False ,filePath=None):
    '''
    输出指定的对象的属性到文件中
    :param module: 指定的模块或类
    :param recreate: 是否重新创建
    :param filePath: 输出的文件路径 如果是目录文件名就是【对象名.的属性.property】
    :return:
    '''
    ## 将module 的属性输出到文件 module的属性.proper 中
    fileName = '%s的属性.property' % module.__name__
    if filePath != None:
        fd = Path(filePath)
        ## 判断是否为目录
        if fd.is_dir():
            fileName =str(PurePath(fd) / PurePath(fileName))
        else :
            fileName = filePath

    #创建文件
    p = Path(fileName)
    if not p.exists() or recreate == True:
        print('属性将读入到文件: ', fileName)
        f = open(fileName, 'a')
        print(dir(module), file=f)
        print('详细的属性如下:',file=f)
        print('------------------------',file=f)
        for p in dir(module):
            print(p, file=f)
        f.close()
    else :
        print('文件[ %s ]已经创建了' % fileName)

## test dode
if __name__ == '__main__':
    outAttr2f(Path,filePath='d:/')