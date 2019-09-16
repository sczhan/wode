
"""
匹配一行文字中所有开头字母 /w
"""
import re
s = "i love you but you don\'t love me"

content = re.findall(r"\b\w", s)
print(content)

# 匹配一行文字中所有数字开头的内容  /d
s1 = "i 22love you but 77you don\'t66  7love me55"
content = re.findall(r"\b\d", s1)
print(content)

# 匹配只含字母和数字的行
s2 = "i love you \n2222kkk but \ndefe23u you \n2324ddd"
content = re.findall(r"\w+", s2, re.M) # re.M匹配多行
print(content)


# 写一个正则表达式, 使其匹配一下字符 "but, hat, hit , hut"
s3 = "but, hat, hit , hut, OOp"
content = re.findall(r"..t", s3)
print(content)

# 提取每行中完整的年月日和时间段
s4 = "se2332  1998-4-15 22:47:47  kjks59898-89 2019-09-16 20:46:20"
content = re.findall(r"(\d{4}-\d{1}-\d{2} \d{2}:\d{2}:\d{2}|\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", s4)
print(content)


# 提取电子邮件格式
s5 = "xxx@gmail.com  xxx@qq.com  www.baidu.com 999.com  175@165.com"
content = re.findall(r"\w+@\w+.com", s5)
print(content)

# 把以上合法的邮件替换成自己的邮件
s6 = "xxx@gmail.com  xxx@qq.com  www.baidu.com 999.com  175@165.com"
content = re.sub(r"\w+@\w+.com", "sczhan@qq.com", s6)
print(content)


# 使用正则提取字符串中的单词
s7 = "i love you not because who ww123  123 of 458djkl not"
content = re.findall(r"\b[a-zA-Z]+\b", s7)
print(content)

# match search
content = re.match(r"[a-zA-Z]+\b", s7)
print(content.group())
content = re.search(r"^[a-zA-Z+\b]", s7)
print(content)


# 使用正则提取字符串中的单词
p = re.compile(r"\b[a-zA-Z]+\b")
s7 = "i love you not because who ww123  123 of 458djkl not"
content = p.findall(s7)
print(content)
