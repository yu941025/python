__author__ = 'Administrator'
'''ajax： 简单的说，就是一段js代码，通过这段代码，可以让页面发送异步的请求，或者向服务器发送一个东西，即和服务器进行交互

对于ajax：
1.一定会有 url，请求方法(get, post)，可能有数据
2.一般使用 json 格式'''
# 爬取豆瓣电影数据
# 了解ajax的爬取方式
# https://movie.douban.com/
from urllib import request
import json
hhh=[]
for start in range(0,280,20):
    hhh.append(start)
hhh.append(276)
aaa=[]
a=open('a.txt','w')
for start in hhh:
    url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={}&limit={}'.format(start,20)
    rep=request.urlopen(url)
    data = rep.read().decode('utf-8')

    data=json.loads(data)
    #print(data)

    for tttt in data:
        '''print('排名',tttt['rank'],'\n',
            '电影名',tttt['title'],'\n',
            '类型',tttt['types'],'\n',
            '主演',tttt['actors'],'\n',
            '分数',tttt['score'],'\n','----------------------')'''
        h={'排名':tttt['rank'], '电影名':tttt['title'],'类型':tttt['types'],'主演':tttt['actors'],'分数':tttt['score']}
        aaa.append(h)
for i in aaa:
    for key,value in i.items():
        print(str(key)+str(value))
        if '\u2022'in str(value):
            str(value).replace('\u2022',u' ')
            a.write(str(key)+str(value)+'\n')
        elif '\xf4'in str(value):
            str(value).replace('\xf4',u' ')
            a.write(str(key)+str(value)+'\n')
        a.write(str(key)+str(value)+'\n')
        a.write('-------------')