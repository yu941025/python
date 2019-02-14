__author__ = 'Administrator'
'''ProxyHandler处理（代理服务器），使用代理IP，是爬虫的常用手段，通常使用UserAgent 伪装浏览器爬取仍然可能被网站封了IP，但是我们使用代理IP就不怕它封了我们的IP了

获取代理IP的的网站：
www.goubanjia.com
www.xicidaili.com
使用代理来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多很多
需要使用，从上面的网站拷贝
基本使用步骤
1.设置代理地址
2.创建ProxyHandler
3.创建Opener
4.安装Opener
案例v11proxy文件：
https://xpwi.github.io/py/py%E7%88%AC%E8%99%AB/py11proxy.py
'''
# 使用代理服务器访问猫眼
# https://maoyan.com/
from urllib import request,error
if __name__=='__main__':
    url = "https://baidu.com/"
    # 1.设置代理地址
    proxy={"http":'218.60.8.83:3129'}
    # 2.创建ProxyHandler
    proxy_hendle=request.ProxyHandler(proxy)
    # 3.创建Opener
    opener=request.build_opener(proxy_hendle)
    # 4.安装Opener
    request.install_opener(opener)
    try:
        rsp=request.urlopen(url)
        res=rsp.read().decode()
        print(res)
    except error.HTTPError as e:
        print(e)
        print('1')
    except Exception as e:
        print(e)
        print('2')

