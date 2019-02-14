__author__ = 'Administrator'
'''功能：
1.解析HTML：使用 etree.HTML(text) 将字符串格式的 html 片段解析成 html 文档
2.读取xml文件
3.etree和XPath 配合使用'''
#lxml-etree 的使用
'''
from lxml import etree
'''
text = '''
<div>
    <ul>
        <li class="item-0"><a href="0.html">item 0 </a></li>
        <li class="item-1"><a href="1.html">item 1 </a></li>
        <li class="item-2"><a href="2.html">item 2 </a></li>
        <li class="item-3"><a href="3.html">item 3 </a></li>
        <li class="item-4"><a href="4.html">item 4 </a></li>
        <li class="item-5"><a href="5.html">item 5 </a></li>
    </ul>
</div>
''''''
# 利用 etree.HTML 把字符串解析成 HTML 文件
html=etree.HTML(text)
s=etree.tostring(html).decode()
print(s)
# lxml-etree读取文件
from lxml import etree
xml=etree.parse('./py24.xml')
sxml=etree.tostring(xml, pretty_print=True).decode()
print(sxml)
'''
#etree和XPath 配合使用
from lxml import etree
xml=etree.parse('py24.xml')
print(etree.tostring(xml).decode())
#查找所有book节点
rst=xml.xpath('//book')
print(rst)
# 查找带有 category 属性值为 sport 的元素
rst2=xml.xpath('//book[@category="sport"]')
# 查找带有category属性值为sport的元素的book元素下到的year元素
rst3=xml.xpath('//book[@category="sport"]/year')
