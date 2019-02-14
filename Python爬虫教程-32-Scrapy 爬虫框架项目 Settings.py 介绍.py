__author__ = 'Administrator'
'''关于 proxy 代理 IP 的详细介绍，查看：Python爬虫教程-11-proxy代理IP，隐藏地址（猫眼电影）
获取代理IP 的网站：
www.goubanjia.com
www.xicidaili.com '''

'''很多网站都是相同的内容，比如介绍 python 爬虫的，很多很多，假设爬取到这些的时候，我们就值需要一个，利用 scrapy 的去重功能，防止它对重复网站无限制爬下去
为了防止爬虫陷入死循环，需要去重
即在 spider 中 parse 函数中，返回 Request 的时候加上 dont_filter = False 参数
myspider(scrapy.Spider):
 def parse (...):
   ...
 yield scrapy.Request(url = url, callback = self.parse, dont_filter = False)'''

