
"""
正则结果Match的使用案例
"""
import re

# 以下正则分成了两个组, 以小括号为单位
s = r"([a-z]+) ([a-z]+)"
pattern = re.compile(s, re.I) # re.I表示忽略大小写

m = pattern.match("Hello wrold wide web")
print(m)

# group(0) 表示返回匹配成功的整个字符串
s = m.group(0)
print(s)

# 表示匹配成功的整个字符串跨度
a = m.span(0)
print(a)

# group(1) 表示返回的第一个分组匹配成功的子串
s1 = m.group(1)
print(s1)

# span(1) 返回匹配成功的第一个子串的跨度
a1 = m.span(1)
print(a1)

# 等价于m.group(1), m.group(2)...
s = m.groups()
print(s)
