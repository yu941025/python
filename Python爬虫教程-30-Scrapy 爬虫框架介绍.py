__author__ = 'Administrator'
'''从本篇开始学习 Scrapy 爬虫框架

Python爬虫教程-30-Scrapy 爬虫框架介绍
框架：框架就是对于相同的相似的部分，代码做到不出错，而我们就可以将注意力放到我们自己的部分了
常见爬虫框架：
scrapy
pyspider
crawley
Scrapy 是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中
Scrapy 官方文档
https://doc.scrapy.org/en/latest/
http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
Scrapy 的安装
可以直接在 Pycharm 进行安装
【PyCharm】>【file】>【settings】>【Project Interpreter】>【+】 >【scrapy】>【install】
具体操作截图：

点击左下角 install 静静等待

测试 Scrapy 是否安装成功
进入当前所在的环境
输入 scrapy 命令
截图：

这里就说明安装成功l
Scrapy 概述
包含各个部件
ScrapyEngine：神经中枢，大脑，核心
Scheduler 调度器：负责处理请求，引擎发来的 request 请求，调度器需要处理，然后交换引擎
Downloader 下载器：把引擎发来的 requests 发出请求，得到 response
Spider 爬虫：负责把下载器得到的网页/结果进行分解，分解成数据 + 链接
ItemPipeline 管道：详细处理 Item
DownloaderMiddleware 下载中间件：自定义下载的功能扩展组件
SpiderMiddleware 爬虫中间件：对 spider 进行功能扩展
数据流图：

绿色箭头是数据的流向
由 Spider 开始 Requests, Requests, Responses, Items
爬虫项目大致流程
1.新建项目：scrapy startproject xxx项目名
2.明确需要爬取的目标/产品：编写 item.py
3.制作爬虫：地址 spider/xxspider.py 负责分解，提取下载的数据
4.存储内容：pipelines.py
模块介绍
ItemPipeline
对应 pipelines 文件
爬虫提取出数据存入 item 后，item 中保存的数据需要进一步处理，比如清洗，去虫，存储等
Pipeline 需要处理 process_item 函数
process_item
spider 提取出来的 item 作为参数传入，同时传入的还有 spider
此方法必须实现
必须返回一个 Item 对象，被丢弃的 item 不会被之后的 pipeline
_ init _：构造函数
进行一些必要的参数初始化
open_spider(spider)：
spider 对象对开启的时候调用
close_spider(spider)：
当 spider 对象被关闭的时候调用
Spider
对应的是文件夹 spider 下的文件
_ init _：初始化爬虫名称，start _urls 列表
start_requests：生成 Requests 对象交给 Scrapy 下载并返回 response
parse：根据返回的 response 解析出相应的 item，item 自动进入 pipeline：如果需要，解析 url，url自动交给 requests 模块，一直循环下去
start_requests：此方法尽能被调用一次，读取 start _urls 内容并启动循环过程
name：设置爬虫名称
start_urls：设置开始第一批爬取的 url
allow_domains：spider 允许去爬的域名列表
start_request(self)：只被调用一次
parse：检测编码
log：日志记录
中间件（DownloaderMiddlewares）
什么是中间件？
中间件是处于引擎和下载器中间的一层组件，可以有多个
参照上面的流程图，我们把中间件理解成成一个通道，简单说，就是在请求/响应等传输的时候，在过程中设一个检查哨，例如：
1.身份的伪装： UserAgent，我们伪装身份，不是在开始请求的时候就设置好，而是在请求的过程中，设置中间件，当检测到发送请求的时候，拦下请求头，修改 UserAgent 值
2.筛选响应数据：我们最开始得到的数据，是整个页面，假设某个操作，需要我们过滤掉所有图片，我们就可以在响应的过程中，设置一个中间件
比较抽象，可能不是很好理解，但是过程是其实很简单的
在 middlewares 文件中
需要在 settings 中设置以是生效
一般一个中间件完成一项功能
必须实现以下一个或者多个方法

process_request (self, request, spider)

在请求的过程中被调用
必须返回 None 或 Response 或 Request 或 raise IgnoreRequest
如果返回 None：scrapy 将继续处理 request
如果返回 Request：scrapy 会停止调用 process_request 并冲洗调度返回的 request
如果返回 Response：scrapy 将不会调用其他的 process_request 或者 process _exception，直接将该 response 作为结果返回，同时会调用 process _response
process_response (self, request, spider)

每次返回结果的时候自动调用'''





''''项目的开发的大致流程：
1.明确需要爬取的目标/产品：编写 item.py
2.在 spider 目录下载创建 python 文件制作爬虫：
地址 spider/xxspider.py 负责分解，提取下载的数据
3.存储内容：pipelines.py
Pipeline.py 文件
对应 pipelines 文件
爬虫提取出数据存入 item 后，item 中保存的数据需要进一步处理，比如清洗，去虫，存储等
Pipeline 需要处理 process_item 函数
process_item
spider 提取出来的 item 作为参数传入，同时传入的还有 spider
此方法必须实现
必须返回一个 Item 对象，被丢弃的 item 不会被之后的 pipeline
_ init _：构造函数
进行一些必要的参数初始化
open_spider(spider)：
spider 对象对开启的时候调用
close_spider(spider)：
当 spider 对象被关闭的时候调用
Spider 目录

对应的是文件夹 spider 下的文件
_ init _：初始化爬虫名称，start _urls 列表
start_requests：生成 Requests 对象交给 Scrapy 下载并返回 response
parse：根据返回的 response 解析出相应的 item，item 自动进入 pipeline：如果需要，解析 url，url自动交给 requests 模块，一直循环下去
start_requests：此方法尽能被调用一次，读取 start _urls 内容并启动循环过程
name：设置爬虫名称
start_urls：设置开始第一批爬取的 url
allow_domains：spider 允许去爬的域名列表
start_request(self)：只被调用一次
parse：检测编码
log：日志记录
---------------------
作者：肖朋伟
来源：CSDN
原文：https://blog.csdn.net/qq_40147863/article/details/82389734
版权声明：本文为博主原创文章，转载请附上博文链接！'''''
