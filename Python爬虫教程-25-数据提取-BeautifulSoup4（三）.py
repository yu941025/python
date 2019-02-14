__author__ = 'Administrator'
'''css 选择器
使用 soup.select 返回一个列表
通过标签名称：soup.select(“title”)
通过类名：soup.select(“.centent”)
id 查找：soup.select(“#name_id”)
组合查找：soup.select(“div #input_content”)
属性查找：soup.select(“img[class=’photo’]”)
获取tag内容：tag.get_text
'''
from urllib import request
from bs4 import BeautifulSoup
url='http://www.baidu.com/'
rsp=request.urlopen(url)
content=rsp.read()


soup=BeautifulSoup(content,'lxml')
content=soup.prettify()
print('===='*12)
titles=soup.select('title')
print(titles[0])
print('===='*12)
meta=soup.select("meta[content='always']")
print(meta[0])
