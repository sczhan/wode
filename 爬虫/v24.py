
"""
python 中正则模块是re
使用大致步骤:
1.  compile 函数讲正则表达式的字符串使以为一个Pattern对象
2. 通过Pattern对象的一系列方法对文本进行匹配, 匹配结果是一个Match对象
3. 用Match对象的方法,对结果进行操作
"""
import re

# \d 表示数字
# 后面+号表示这个数字可以出现一次或者多次
# r 表示后面不转义
s = r"\d+" # r 表示后面是原生字符串,后面不需要转义

# 返回一个Pattern对象
pattern = re.compile(s)

# 返回一个Match对象
# 默认找到一个匹配返回
m = pattern.match("one21two2three3")

print(type(m))
# 默认匹配从头部开始, 所以此次结果为None
print(m)

# 后面为位置参数 含义是从哪个位置开始查找,找到哪个位置结束
ms = pattern.match("one21two2three3", 8, 10)

print(type(ms))
print(ms)

print(ms.group())
print(ms.start(0))
print(ms.end(0))
print(ms.span(0))