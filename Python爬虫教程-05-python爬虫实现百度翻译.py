__author__ = 'Administrator'
from urllib import request,parse
import json

def fanyi(keyword):
    base_url = 'https://fanyi.baidu.com/sug'

    # 构建请求对象
    data = {
        'kw': keyword
    }
    data = parse.urlencode(data)#urlencode是一个函数，可将字符串以URL编码，用于编码处理。

    a=parse.unquote(data)


    # 模拟浏览器
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=header)
    res = request.urlopen(req)
    print(res)

    # 获取响应的json字符串
    str_json = res.read().decode('utf-8')



    # 把json转换成字典
    myjson = json.loads(str_json)


    info = myjson['data'][0]['v']
    print(info)

if __name__=='__main__':
    while True:
        keyword = input('请输入翻译的单词：')
        if keyword == 'q':
            break
        fanyi(keyword)

