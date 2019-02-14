__author__ = 'Administrator'
from urllib import request,parse
from http import cookiejar
cookie=cookiejar.MozillaCookieJar()
cookie.load('py15renrenCookie.txt',ignore_expires=True,ignore_discard=True)
cook_hander=request.HTTPCookieProcessor(cookie)
http_hander=request.HTTPHandler()
https_hander=request.HTTPSHandler()
opener=request.build_opener(cook_hander,http_hander,https_hander)
def getHomePage():
    url='http://www.renren.com/967487029/profile'
    rsp=opener.open(url)
    html=rsp.read().decode()
    with open("py13rsp.html", "w", encoding="utf-8")as f:
        # 将爬取的页面
        print(html)
        f.write(html)

if __name__ == '__main__':

    getHomePage()
