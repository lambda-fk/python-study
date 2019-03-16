
import xml.etree.ElementTree as ET

##
tree = ET.parse('./xml文件/exam.xml')
root = tree.getroot() ## 根，最外层的根
print('根节点为:',root.tag)

## 遍历根节点下的所有孩子节点
for child in root:
    ## 读取的属性 为 attrib ，结果是一个字典,存储着所有属性，如果没有就是一个空字典
    print(child.tag,child.attrib)
    for i in child:
        # text 为标签中间围着的内容
        print(i.tag,i.attrib,i.text)


## 修改标签
for node in root.iter('other'):
    #添加text
    node.text='添加额外信息'
    # 添加节点的 attrib 属性
    node.set('updated',"yes")

## 修改完成之后重新写入
tree.write('./xml文件/exam.xml')

## 删除节点
for stu in root.findall('student'):
    ## 读取节点下 age标签的文本
    age = stu.find('age').text
    if int(age) < 22:
        root.remove(stu)
tree.write('./xml文件/exam.xml')