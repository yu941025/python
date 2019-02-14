__author__ = 'Administrator'
'''动态前端页面 ：
JavaScript：
JavaScript一种直译式脚本语言，是一种动态类型、弱类型、基于原型的语言，内置支持类型。它的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，最早是在HTML（标准通用标记语言下的一个应用）网页上使用，用来给HTML网页增加动态功能
jQuery：
jQuery是一个快速、简洁的JavaScript框架，是继Prototype之后又一个优秀的JavaScript代码库（或JavaScript框架）。jQuery设计的宗旨是“write Less，Do More”，即倡导写更少的代码，做更多的事情。它封装JavaScript常用的功能代码，提供一种简便的JavaScript设计模式，优化HTML文档操作、事件处理、动画设计和Ajax交互
ajax：
Ajax 即“Asynchronous Javascript And XML”（异步 JavaScript 和 XML），是指一种创建交互式网页应用的网页开发技术。
Ajax = 异步 JavaScript 和 XML（标准通用标记语言的子集）。
Ajax 是一种用于创建快速动态网页的技术。
Ajax 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。
通过在后台与服务器进行
DHTML：
DHTML是Dynamic HTML的简称，就是动态的html（标准通用标记语言下的一个应用），是相对传统的静态的html而言的一种制作网页的概念。所谓动态HTML（Dynamic HTML，简称DHTML），其实并不是一门新的语言，它只是
HTML、CSS和客户端脚本的一种集成，即一个页面中包括html+css+javascript（或其它客户端脚本），其中css和客户端脚本是直接在页面上写而不是链接上相关文件。DHTML不是一种技术、标准或规范，只是一种将目前已有的网
页技术、语言标准整合运用，制作出能在下载后仍然能实时变换页面元素效果的网页设计概念
'''
# Selenium 的使用
# 通过 WebDriver 操作百度进行查找
from selenium import webdriver
import time
# 通过 Keys 模拟键盘
# 也就是放入需要输入的东西，就不用键盘输入了
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.baidu.com")
print("Title: {0}".format(driver.title))