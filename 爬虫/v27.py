
"""
findall 练习
"""
import re

pattern = re.compile(r"\d+")

s = pattern.findall("i am 18 years and 177 and 55")
print(s)

s = pattern.finditer("i am 18 years and 177 and 55")
print(type(s))
print(s)

for item in s:
    # print(item)
    print(item.group())

