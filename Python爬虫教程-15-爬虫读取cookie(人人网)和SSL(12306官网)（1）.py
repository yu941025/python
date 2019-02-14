__author__ = 'Administrator'
from urllib import request

import ssl

# 利用非认证上下文环境替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.12306.cn/mormhweb/"
rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)
'''ssl证书就是指遵守ssl安全套阶层协议的服务器数字证书（SercureSocketLayer）
美国网景公司开发
使用ssl，加密信息
俗称https协议
CA（CertificateAuthority）是数字证书任重中心，是发放，管理，废除数字证书的收信人的第三方机构
遇到不信任的SSL证书，需要单独处理
案例v17ssl文件：
'''