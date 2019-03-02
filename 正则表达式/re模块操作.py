
'''
正则表达式： 匹配字符串
操作对象都是字符串
string提供的方法是完全匹配
所有的正则表达式都是一样的

字符匹配（普通字符，元字符）
元字符：
'''
import re

# findall
print(re.findall('w\w{2}l','hello world'))

# 完全匹配
print('完全匹配')
print(re.findall('qianyue','abcqianyueabc'))
print('字符串的完全匹配...')
print('abcqianyueabc'.find('qianyue')) # 3 ： 返回的是第一次出现的 index

##元字符  11 个元字符
# 元字符 点 . 称为 通配符 : 代指换行符之外的所有字符,一个点只能代指任意的一个字符，指代不了 \n , \r可以指代
print(re.findall('w..l','world'))
print(re.findall('w.l','w\nl'))
print(re.findall('w.l','w\rl'))

## 元字符： 尖角符号  : 表示从开头进行匹配
print(re.findall())

## 元字符: $ 表示从末尾匹配 放置于末尾
print(re.findall('a..x$','sddffggsggabcx'))
print(re.findall('a..x$','addgggabcxy$'))




