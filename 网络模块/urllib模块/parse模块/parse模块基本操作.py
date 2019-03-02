from urllib import parse

url = r'https://blog.csdn.net/fk002008/article/details/87553034?user=fk&pkid=1&type=2'

## 解析 url
rlt = parse.urlparse(url)
print(type(rlt)) ## <class 'urllib.parse.ParseResult'>
print(rlt)
print('scheme :' , rlt.scheme , rlt[0])
print('netloc :' , rlt.netloc , rlt[1])
print('path:' , rlt.path , rlt[2])
print('params:' , rlt.params , rlt[3])
print('query:',rlt.query , rlt[4])
print('fragment' ,rlt.fragment , rlt[5])


## 根据 ParseResult 重新组装url
url = parse.urlunparse(rlt)
print('使用 ParseResult 对象 重新组装的 url :' , url)

## 根据提供的元组重新组装url ,
## 使用这个元组组装的时候注意元素必须是 6 个 ，其中注意这个 params 和 fragment 的位置要注意
## (scheme , netloc , path , params , query , fragment )
url = parse.urlunparse(('https','www.126.com','/lambdafk/books','','user=fk&pkid=2&type=3',''))
print('使用 元组 重新组装的 url :' , url)


## 解析 query 中参数
dd = parse.parse_qs(rlt.query)
print('使用 parse.parse_qs 解析的query参数结果是一个字典 :' , dd)

ll = parse.parse_qsl(rlt.query)
print('使用 parse_qsl 解析的query 参数结果是一个列表:' ,ll)

## 反过来将列表中内容组装成 query 参数
qu  = parse.urlencode([('user', 'fk'), ('pkid', '1'), ('type', '2')])
print(type(qu)) ## 结果是一个 str
print('使用列表组装成的  query 为 ：' , qu)