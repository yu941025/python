__author__ = 'Administrator'
'''URLError 产生的原因：
1.无网络连接
2.服务器连接失败
3.找不到指定的服务器
4.URLError是OSError的子类'''
from urllib import request,error
if __name__=='__main__':
     url = "http://www.baiiiiiiiiiiidu.com/"
     try:
         res=request.Request(url)
         req=request.urlopen(res)
         html=req.read().decode()
     except error.URLError as e:
         print(e.reason)
         print(e)
         print('1')
     except Exception as e:
         print(e)


'''HTTPError
1.是URLError的一个子类
URLError和HTTPError的区别：
HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上的，则引发HTTPError
URLError对应的一般是网络出现问题，包括url问题'''