
import xml.etree.ElementTree as ET

## 创建根节点
new_xml = ET.Element('namelist')

## 创建子节点
name = ET.SubElement(new_xml,'name',attrib={'enrolled':'yes'})
age = ET.SubElement(name,'age',attrib={'checked':'no'})
sex = ET.SubElement(name,'sex')

## 给字节点设置文本
age.text = '31'

## 生成文档树
et = ET.ElementTree(new_xml)

## 创建xml 文件
et.write('./xml文件/生成xml文件.xml',encoding='utf-8',xml_declaration=True)

## 打印生成的格式
ET.dump(new_xml)