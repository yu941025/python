__author__ = 'Administrator'
import requests
import json

def fanyi(keyword):
    url = 'https://fanyi.baidu.com/sug'

    # 定义请求参数
    data = {
        'kw': keyword
    }
    proxies = {'http': '111.23.10.27:8080'}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

    }

    # 发送请求，抓取信息
    res = requests.post(url,data=data)
    res.encoding='utf-8'
    # 解析结果并输出
    str_json = res.text

    #print(str_json)
    try:
        myjson = json.loads(str_json)
        info=myjson['data'][0]['v']
        print(info)
    except:
        print('输入错误')


if __name__=='__main__':
    while True:
        keyword = input('请输入翻译的单词：')
        if keyword == 'q':
            break
        fanyi(keyword)

