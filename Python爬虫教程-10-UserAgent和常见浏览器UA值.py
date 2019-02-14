__author__ = 'Administrator'
from urllib import request,error
if __name__=='__main__':
    try:
        url = "http://www.baidu.com/"
        req=request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163')
        res=request.urlopen(req)
        html=res.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e.reason)
        print(e)
        print('1')
    except error.URLError as e:
        print(e)
        print(2)
    except Exception as e:
        print(e)
'''UserAgent
包含浏览器信息，用户身份，设备系统信息
UserAgent：用户代理，简称UA，属于headers的一部分，服务器通过UA来判断访问者身份
使用方法：复制粘贴即可
案例v10UA文件：https://xpwi.github.io/py/py%E7%88%AC%E8%99%AB/py10UA.py
！'''