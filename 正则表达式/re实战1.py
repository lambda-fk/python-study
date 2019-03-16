'''

正则表达式方法
'''
import re

# 1: findall 所有结果都返回到一个列表里面
# 2: search: 匹配上返回一个对象，包含了匹配的信息,可以使用 group() 方法拿到返回的结果，只返回匹配到的第一个对象
# 3: match : 只在字符串开始进行匹配
# 4: split:
ret = re.split('[j,s]','djksal')
print(ret) ## ['d', 'k', 'al']
## 拆分的结果是： 先用 j 来拆分成 d 和 ksal , 然后将两部分再用 s 进行拆分 d , k ,al

ret = re.split('[j,s]','sdjksal')
print(ret) # ['', 'd', 'k', 'al']
## 用 j 拆分成  sd 和 ksal ，然后使用 s 再一次去分 ， sd 中的 s 前面是空，所以有空的存在


# 5:sub : 匹配之后进行替换  至少需要3个参数： 规则，被检查字符串 ， 要替换内容
ret = re.sub('p.*y','hello python','java')
print(ret) # java

# 6:compile() : 一种规则应用多次的情况，将规则弄成对象重复使用,将正则表达式编译成正则表达式对象
m = re.compile('p.*y')
ret = m.findall('hello python')
print(ret)# ['py']
