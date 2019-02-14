__author__ = 'Administrator'
from urllib import request
import chardet
if __name__=='__main__':
    url='https://jobs.zhaopin.com/CC375882789J00033399409.htm'
    resp=request.urlopen(url)
    html=resp.read()
    cs=chardet.detect(html)
    print(cs)
    print(html)
    html=html.decode(cs.get('encoding','utf-8'))# 意思是监测到就使用监测到的，监测不到就使用utf-8
