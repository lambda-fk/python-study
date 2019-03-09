
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
print(re.findall('w\w{2}l','hello world')) #['worl']

# 完全匹配
print('完全匹配...')
print(re.findall('qianyue','abcqianyueabc'))
print('字符串的完全匹配...')
print('abcqianyueabc'.find('qianyue')) # 3 ： 返回的是第一次出现的 index

##元字符  11 个元字符
print('re的11个元字符操作...')
# 1元字符 点 . 称为 通配符 : 代指换行符之外的所有字符,一个点只能代指任意的一个字符，指代不了 \n , \r可以指代
print(re.findall('w..l','world')) #['worl']
print(re.findall('w.l','w\nl')) #[] 匹配不上换行符的 , 可以通过修改第三个参数flags来让指定让其匹配上
print(re.findall('w.l','w\rl'))#['w\rl']

## 2元字符： 尖角符号 ^ : 表示从开头行首进行匹配
print('元字符 ^ 开头匹配规则...')
print(re.findall('^h...o','hdfgo')) # ['hdfgo'] 表示从开始进行匹配

## 3元字符: $ 表示从末尾匹配 放置于末尾
print('元字符 $ 末尾匹配规则...')
print(re.findall('a..x$','sddffggsggabcx')) # ['abcx']
print(re.findall('a..x$','addgggabcxy$')) #[]

## 4.元字符:  * : 重复匹配,可代表任意个数的重复 表示重复匹配 0次到无穷大次
print('元字符 * 重复匹配...')
print(re.findall('ba*','dfggsgsgsbaaaaaaa')) #['baaaaaaa']
# 如果是 .* ，那么表示所有的进行匹配，为什么是两个值呢，因为可以匹配 0 次的存在
print(re.findall('.*','dfggsgsgsbaaaaaaa')) #['dfggsgsgsbaaaaaaa', '']

print(re.findall('h.*l','hellol')) # ['hellol'] 所以 .* 表示了中间是任意字符串的
print(re.findall('h*l','hellol')) # ['l', 'l', 'l'] # 因为要重复 h 为0-无穷次 ， 所以 3个 l 都出来了
print(re.findall('h*o','xxoxhello')) # ['o', 'o'] # 因为重复 h 为 0-无穷从，所以2个 o 都出来了
print(re.findall('h*l','hhhhhhhhl')) #['hhhhhhhhl']
###  .* 和 * 的区别在于： .* 表示了重复前面的任意字符无穷次
###  * 表示了前面指定的字符无穷次 , 主要是前面的字符是指定的

# 5.元字符 + : 表示重复匹配 [1,无穷] , 至少有一个 , 只对其前面的字符有用
print('元字符 + 的使用...')
print(re.findall('ab+','adddac')) # []
print(re.findall('ab+','abbcabhhh')) #['abb', 'ab']
print(re.findall('a+b','aaaaaaabhhhhffabfb')) #['aaaaaaab', 'ab']

# 6.元字符 ? : 表示重复了 [0,1] 次 , 也表示了重复它前面的字符 0-1 次
print('元字符 ? 的使用...')
## 表示了以 字串 前面有 0-1 个a结尾是b 的字串
print(re.findall('a?b','aaaabhghabfb')) #['ab', 'ab', 'b'] 因为 末尾的 fb 也是满足的，表示重复0次

# 7 元字符 {} : 表示重复了指定次数 ， 作用于它前面的字符重复指定的次数或者是一个范围
print('元字符{} 的使用...')
print(re.findall('a{5}b','aaaaabab')) # ['aaaaab']
print(re.findall('a{1,3}b','aabdfaaab')) # ['aab', 'aaab']

####   * 表示 {0,正无穷}  , + 表示了 {1,正无穷}  ? 表示{0,1}

## 8: 元字符 [] : 表示字符集
print('\n元字符 [] 的使用...')
print(re.findall('a[c,d]x','acx')) # ['acx'] 表示的是 c或d ,2选1 的形式
print(re.findall('a[c ,d]x','adx')) # ['adx'] ，其中每个字符是可以带空格的不影响
print(re.findall('a[c,d]x','acdx')) # []
## 下面因为规则 [a-z] 只是一个 ，所以结果是单个 形式出现
print(re.findall('[a-z]','sdfbg')) # ['s', 'd', 'f', 'b', 'g']

##取消 元字符的特殊功能 , 将元字符写入到 [] 中就没有了 其特殊功能了
## 但是有例外情况 \  ^  -  三个是不能取消的
print(re.findall('a[w,*]','a*l')) # ['a*']
print(re.findall('a[l,,f]','al,,d'))
print(re.findall('[1-9,a-z,A-Z]','123abcTG')) #['1', '2', '3', 'a', 'b', 'c', 'T', 'G']
print(re.findall('[1-9a-zA-Z]','123abcTG')) #['1', '2', '3', 'a', 'b', 'c', 'T', 'G']
## [] 中加入了 尖角号 ^ 之后 表示取反的意思
print(re.findall('[^t]','abctg')) # ['a', 'b', 'c', 'g']  没有 t 的
## []之内的^ 表示了所有的非 , 注意了 此时 ^ 后面都是非 ，包括那个逗号,不要认为它是分隔符
print(re.findall('[^4,5]','as4g5')) # ['a', 's', 'g']
print(re.findall('[^4,5]','as4g5,,k')) # ['a', 's', 'g', 'k']

## 9: 元字符 \  :
print('\n元字符 \\ 的使用...')
## \ 后面跟元字符 去掉元字符的特殊功能
## \ 后面跟普通字符实现特殊功能 , 转义了 如 \d  表示数字, \w 表示字母
temp ='''
\d: 表示数字
\D: 匹配任何非数字字符 等价于 [^0-9]
\s: 匹配任何空白字符
\S : 匹配任何非空白字符
\w: 匹配任何字母数字字符
\W: 匹配任何非字母数字字符

\b: 匹配任何一个单词边界，也就是单词和空格之间的位置 ,空格，特殊字符$,# 也算的
    需要注意的是 \b 本身在python 中有转义字符的，直接使用 \b 是无法得的re 中的\b的
    因此re使用 \b 的时候，需要使用 r'\b' 这样得到就是原生的 \b 字符串
'''
print(temp)

## 匹配11 个数字
print(re.findall('\d{11}','wsgsgsg12345678901')) # ['12345678901']
print(re.findall('\d{11}','wsgsgsg12345678901df44444444455')) # ['12345678901', '44444444455']
print(re.findall('\D','wsgsgsg12345678901')) # ['w', 's', 'g', 's', 'g', 's', 'g']
print(re.findall('I','I am LIST')) # ['I', 'I']
print(re.findall('I\b','I am LIST')) # []
print(re.findall(r'I\b','I am LIST')) # ['I']
print(re.findall(r'I\b','I am LI$ST')) # ['I', 'I']
print(re.findall(r'I\b','I am LI#ST')) # ['I', 'I']

# \ 加上元字符去除掉 元字符的特殊功能
# search 只会返回第一次出现的
print(re.search('\*','a*b')) #<re.Match object; span=(1, 2), match='*'> 表示从[1,2) 的范围
ret = re.search('\*','aa*b')
print(ret.group()) # *

## 对于 \b ,\\ 这种匹配的，都需要 使用原始字符串来进行的
## 因为 re模块中的 \ 是有特殊功能的
## python中的 \ 也算有特殊意义的
## 因此一旦使用 python 的re 模块时候 ， 就要注意了
## python层面的 \\ 表示一个 \ ,re模块需要的 \ 也需要 \\ 给出的，所以在
## re 模块里面使用 \\ 的时候，是需要给出 \\\\ 四个反斜杠才可以的表示最终的 \\
## 所以为了简便使用 可以使用 r开头的字符串，表示原生的字符串不用进行转义
## 所以 \b , \\ 这种的字符串如果进行re的使用时候 加上 r 指定规则


## 10 元字符 () :  分组
print('() 的使用...')
## () 将内部的东西看成一个整体进行
ret = re.search('(as)+','sdafas')
print(ret.group()) # as

## 分组 给组起名字 (?P<id>\d{3})
## 其中 ?P 表示要起名字 <>之内的就是 组的名字，然后可以通过 search结果的group指定组名访问
## 这种语法必须 使用 (?P<组名>组的匹配规则串) 来进行
ret = re.search('(?P<id>\d{3})','abcd456')
print(ret.group('id')) ## 456
## 可以多分几个组
ret = re.search('(?P<id>\d{4}):(?P<name>\w{4})','FT-4567:ttrt')
print(ret.group('id')) # 4567
print(ret.group('name')) # ttrt



## 11 元字符  | : 或
print('| 的使用方法...')
## 注意使用 search的时候只会返回第一个匹配的内容
ret = re.search('(as)| 3','3as') #3
print(ret.group())

print(re.findall('(as)|x','asx')) # ['as', '']