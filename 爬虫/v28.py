"""
search 练习
"""
import re

s = r"\d+"

pattern = re.compile(s)

m = pattern.search("one1two2three3four456")
print(m.group())

# 参数表明搜查的起始范围
m = pattern.search("one1two2three3four456", 4, 50)
print(m.group())
