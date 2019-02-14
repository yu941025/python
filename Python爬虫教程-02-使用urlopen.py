__author__ = 'Administrator'
'''urllib.request：打开和读取urls
urllib.error：包含urllib.request产生的常见错误，使用try捕捉
urllib.parse：包含解析url的方法
urllib.robotparse：解析robots.txt文件
robots：机器人协议，放在网站的开头，供给爬虫读取，当爬虫读到robots之后，就知道那些是允许爬取的数据，哪些是禁止爬取的数据
（爬虫道德问题：1.不许过频繁爬取 2.不许爬取禁止内容）
'''
from urllib import request
if __name__=='__main__':
    url="https://jobs.zhaopin.com/CC375882789J00033399409.htm"
    response=request.urlopen(url)
    html=response.read()
    a=html.decode()
    print(a)
