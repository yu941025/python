__author__ = 'Administrator'
'''正则使用步骤：
1.使用 compile 函数将正则表达式的字符串编译成一个 pattern 对象
2.通过 pattern 对象的一些方法对文本进行匹配，匹配结果是一个 match 对象
3.用 match 对象的方法，对结果进行操作
正则的常用方法：
match：从开始位置开始查找，一次匹配，即1次匹配成功则退出
search：从任何位置开始查找，一次匹配
findall：全部匹配，返回列表
finditer：全部匹配，返回迭代器
split：分割字符串，返回列表
sub：替换
匹配中文
中文是Unicode编码(utf-8也是Unicode编码)，范围：主要在[u4e00-u9fa5]
中文全角逗号一类的不在[u4e00-u9fa5]范围内
贪婪与非贪婪模式
贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配
非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配
python里面数量词默认是贪婪模式
例如：
查找文本abbbbbbbccc
re结果是： ab*
贪婪模式结果是：abbbbbbb
非贪婪模式结果是：a
'''
# 正则结果match的使用案例
# 以下正则分成2个组，以小括号为单位
# [a-z]表示出现小写a-z任意字母都可以，+表示至少出现1次
# 两组之间有一个空格，表示匹配的两个英文字符之间有空格
#match的使用
import re
s=r"([a-z]+) ([a-z]+)"
pattern=re.compile(s,re.I)# s, I表示忽略大小写
m= pattern.match("Hello world wide web")
s=m.group(0)
print(s)
a=m.span(0)
print(a)
h=m.group()
print(type(h))
#search的使用
import re
s=r'\d+'
pattern=re.compile(s)
m=pattern.search('one12two34three56')
print(m.group(0))
m = pattern.search("one12two34three56", 10, 40)
print(m.group(0))
#findall，finditer的基本使用
import re
s=r'\d+'
pattern=re.compile(s)
m=pattern.findall('I am 18 years old, and 185 high')
print(m)
n = pattern.finditer("I am 18 years old, and 185 high")
print(type(n))
for i in n :
    print(i.group())


#匹配中文
import re
hello=r'你好，再见陌生人,号啊号，是 撒，是'
pattern=re.compile(r'[\u4e00-\u9fa5]+')
m=pattern.findall(hello)
print(m)
import re
pattern=re.compile(r'[\u4e00-\u9fa5]+')
s=pattern.findall('你好傻逼')
print(s)