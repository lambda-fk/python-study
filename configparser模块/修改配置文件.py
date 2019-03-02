import configparser

config = configparser.ConfigParser()
config.read('sample.ini')

## 所有的操作都从 config那里获取即可

## 添加一个section
config.add_section('add')
config.set('add','test','add()')
config.write(open('sample.ini','w')) #通过重新写入文件达到修改目的

## 删除一个 section
config.remove_section('add')
config.write(open('sample.ini','w')) #通过重新写入文件达到修改目的

## 删除具体的一个 option
#config.remove_option('section名字','option')
#config.write()  # 重新写入文件

## 修改 option 内容
#config.set('section名字','option','value')
#config.write()  # 重新写入文件
