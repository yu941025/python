__author__ = 'Administrator'
'''自动使用cookie的方法，告别手动拷贝cookie
http模块包含一些关于cookie的模块，通过他们我们可以自动的使用cookie
CookieJar
管理存储Cookie，向传出的http请求添加cookie
这里Cookie存储在内存中，CookieJar实例回收后cookie将消失
FileCookieJar(filename, delayload=None, policy=None)
使用文件管理cookie
filename是保存cookie的文件
MozillaCookieJar(filename, delayload=None, policy=None)
创建Mocilla浏览器cookie.txt兼容的FileCookieJar实例

火狐Firefox浏览器需要单独处理
LwpCookieJar(filename, delayload=None, policy=None)
创建于libww-per标准兼容的Set-Cookie3格式的FileCookieJar
它们之间的关系： CookieJar–>FileCookieJar–>MozillaCookieJar & LwpCookieJar
'''
'''自动使用cookie登录，使用步骤：
1.打开登录页面后自动通过用户名密码登录
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
# 创建cookiejar的实例
cookie=cookiejar.CookieJar()
# 常见cookie的管理器
cookie_hander=request.HTTPCookieProcessor(cookie)
# 创建http请求的管理器
http_hander=request.HTTPHandler()
# 生成https管理器
https_hander=request.HTTPSHandler()
# 创建请求管理器
opener=request.build_opener(http_hander,https_hander,cookie_hander)
def login():
    # 负责首次登录，输入用户名和密码，用来获取cookie
    url='http://www.renren.com/PLogin.do'
    ID=input("请输入账号：")
    PASSWORD=input('请输入密码：')
    data={
        # 从input标签的name获取参数的key，value由输入获取
        "email":ID,
        'password':PASSWORD
    }
    #data编码
    data=parse.urlencode(data)
    #创建一个请求对象
    req=request.Request(url,data=data.encode('utf-8'))
    # 使用opener发起请求
    res=opener.open(req)
    print(res.read().decode('utf-8'))
    # 以上代码就可以进一步获取cookie了，cookie在哪呢？cookie在opener里
def getHomePage():
    # 地址是用在浏览器登录后的个人信息页地址
    url='http://www.renren.com/832618644/profile'
    # 如果已经执行login函数，则opener自动已经包含cookie
    #rsp=opener.open()
    request.install_opener(opener)
    rsp=request.urlopen(url)
    html=rsp.read().decode()
    with open('rsp1.html','w',encoding="utf-8") as f:
        print(html)
        f.write(html)

if __name__=='__main__':
    login()
