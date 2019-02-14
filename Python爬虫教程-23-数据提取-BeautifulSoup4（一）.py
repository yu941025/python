__author__ = 'Administrator'
from urllib import request
from bs4 import BeautifulSoup
url='http://www.baidu.com/'
rsp=request.urlopen(url)
content=rsp.read().decode()
soup=BeautifulSoup(content,'lxml')
#自动解码
content=soup.prettify()
print("soup.meta:\n", soup.meta)
print("=="*12)
print("soup.meta.name:\n",soup.meta.name)
print("soup.meta.attrs:\n",soup.meta.attrs)
print("=="*12)
print("soup.meta.attrs['content']:\n",soup.meta.attrs['content'])