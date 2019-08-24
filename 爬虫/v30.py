
"""
安装lxml
"""
from lxml import etree

"""
用lxml来解析HTML代码
"""

text = """
<div>
    <ul>
        <li class="item-0"> <a href="1.html"> first item </a></li>
        <li class="item-0"> <a href="2.html"> first item </a></li>
        <li class="item-0"> <a href="3.html"> first item </a>
    </ul>
</div>
"""

# 利用etree.HTML把字符串解析成HTMl文档
html = etree.HTML(text)
s = etree.tostring(html)
print(s)