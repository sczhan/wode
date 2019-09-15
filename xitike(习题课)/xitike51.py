
"""
匹配一行文字中所有开头字母 /w
"""
import re
s = "i love you but you don\'t love me"

content = re.findall(r"\b\w", s)
print(content)

# 匹配一行文字中所有数字开头的内容  /d
s1 = "i 22love you but 77you don\'t66  7love me"
content = re.findall(r"\b\d", s1)
print(content)

# 匹配只含字母和数字的行
s2 = "i love you \n2222kkk but \ndefe23u you \n2324ddd"
content = re.findall(r"\w+", s2, re.M) # re.M匹配多行
print(content)