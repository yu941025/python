__author__ = 'Administrator'
'''研究request的返回值，输出返回值类型，打印内容
geturl：返回请求对象的url
info：请求返回对象的meta信息
getcode：返回的http code
py04v3.py文件：https://xpwi.github.io/py/py%E7%88%AC%E8%99%AB/py04v3.py
'''
from urllib import request
if __name__=='__main__':
    url = 'https://jobs.zhaopin.com/CC375882789J00033399409.htm'
    resp=request.urlopen(url)
    print(resp.geturl())
    print(type(resp))
    print(resp.info())
    print(resp.getcode())