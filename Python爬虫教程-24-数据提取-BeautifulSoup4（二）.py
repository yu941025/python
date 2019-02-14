__author__ = 'Administrator'
'''遍历文档对象
contents：tag 的子节点以列表的方式输出
children：子节点以迭代器形式返回
descendants：所有子孙节点
string：用string打印出标签的具体内容，不带有标签，只有内容'''
'''from urllib import request
from bs4 import BeautifulSoup
url='http://www.baidu.com/'
rsp=request.urlopen(url)
content=rsp.read()
soup=BeautifulSoup(content,'lxml')
#自动解码
content=soup.prettify()
print('=='*12)
for node in soup.head.contents:
    if node.name=='meta':
        print(node)
    if node.name=='title':
        print(node.string)
print('==='*12)'''

from urllib import request
from bs4 import BeautifulSoup
import re
url='http://www.baidu.com/'
rsp=request.urlopen(url)
content=rsp.read()
soup=BeautifulSoup(content,'lxml')
content=soup.prettify()
print('==='*12)
tags=soup.find_all(re.compile('^me'),content='always')
print(tags)
for i in tags:
    print(i)