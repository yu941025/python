__author__ = 'Administrator'
'''自动使用cookie登录，使用步骤：
1.打开登录页面后，通过用户名密码登录
2.自动提取反馈回来的cookie
3.利用提取的cookie登录个人信息页面
创建cookiejar实例
生成cookie的管理器
创建http请求管理器
创建https请求的管理器
创建请求管理器
通过输入用户名和密码，获取cookie
'''
from urllib import request,parse
from http import cookiejar
#cookie作为一个变量打印出来
cookie=cookiejar.CookieJar()
cookie_hander=request.HTTPCookieProcessor(cookie)
http_hander=request.HTTPHandler()
https_hander=request.HTTPSHandler()
opener = request.build_opener(http_hander,https_hander,cookie_hander)
request.install_opener(opener)
def login():
    url='http://www.renren.com/PLogin.do'
    id=input('请输入账号：')
    pw=input('请输入密码：')
    data={
        'email':id,
        'password':pw
    }
    data=parse.urlencode(data)
    req=request.Request(url,data=data.encode('utf-8'))
    res=request.urlopen(req)
def getHomePage():
    url='http://www.renren.com/967487029/profile'
    rsp=opener.open(url)
    html=rsp.read().decode()
    with open("rsp1.html", "w", encoding="utf-8")as f:
        # 将爬取的页面
        print(html)
        f.write(html)
if __name__=='__main__':
    login()
    print(cookie)
    for i in cookie:

        print(i)
'''下面介绍常用的属性

cookie的属性
name：名称
value：值
domain：可以访问此cookie的域名
path：可以访问此cookie的页面路径
expires：过期时间
size：大小
http：字段'''