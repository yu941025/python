__author__ = 'Administrator'
'''常见反爬虫手段：
验证码
1.简单图片，扭曲数字验证码
2.中文顺序点击
3.动态验证码
4.滑动验证：滑动小方块到缺口
5.语音验证
6.极验验证：官网：http://www.geetest.com/
根据鼠标轨迹，判定是机器人还是用户，很强大的验证机制
对于极验是很厉害的拦截机器人手段，好像是使用人工智能机器学习，当然自己想做验证的话建议使用。对于验证有反爬虫，就有可能有反反爬虫
'''
'''爬虫-验证码识别
通用方法：
1.下载网页和验证码，或截图
2.然后手动输入验证码
对于简单图片
1.使用图像识别软件或者文字识别软件
2.可以使用第三方图像验证码破解网站
比如：超级鹰：http://www.chaojiying.com/
对于极验，官网：http://www.geetest.com/
可以模拟鼠标移动，具体的方法我还不清楚
'''
import pytesseract as pt
from PIL import Image
image=Image.open('123.jpg')
text=pt.image_to_string(image)
print(text)
#想看训练的部分，点击：Tesseract-OCR-02-使用 jTessBoxEditor 提高文字识别准确率
