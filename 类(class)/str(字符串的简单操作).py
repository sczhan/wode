# + 字符串的连接操作
s1 = "lo"
s2 = "ve"
print(s1+s2)
print("lo"+"ve")


# * 字符串的复制操作
print("#"*20)


# []字符串的索引操作
s3 = "l love you"
print(s3[-1])
print("*"*20)

# [: :] 字符串的切片操作
# [开始索引:结束索引:间隔值] (包含开始,不包含结束)
print(s3[2:6])
print(s3[-8:-4:1])
print(s3[-2:-6:-1])
print("*"*20)

# 切整个字符串
print(s3[:])
print("*"*20)

# 指定开始,不指定结束
print(s3[2:])
print("*"*20)

# 指定结束,不指定开始
print(s3[:6])
print("*"*20)

# 指定开始,不指定结束并给出间隔值
print(s3[2::2])
print("*"*20)

# 指定结束,不指定开始并给出间隔值
print(s3[:6:3])
print("*"*20)

# capitalize() 首字母大写 返回字符串
s = "i love you"
print(s.capitalize())
print("*"*20)


# title() 每个单词的首字母大写 返回字符串
print(s.title())
print("*"*20)

# upper() 将所有字母大写 返回字符串
print(s.upper())
print("*"*20)

# lower() 将所有字母小写  返回字符串
print(s.lower())
print("*"*20)

# swapcase() 大小写互换  返回字符串
s4 = "L Ll"
print(s4.swapcase())
print("*"*20)

# len() 计算字符串长度,不属于字符串的内建函数
print(len(s4))
print("*"*20)

# find() 查找指定字符串,找不到返回-1  第一次找到返回第一次索引值
# index() 查找指定字符串,找不到报错   第一次找到返回第一次索引值
s5 = "akjksdsaaa"
s6 = s5.find("a")
s7 = s5.index("a")
print(s6)
print(s7)
print("#"*20)
s6 = s5.find("w")
# s7 = s5.index("w")  报错
print(s6)
print(s7)
print("#"*20)
s6 = s5.find("a", 2, -1)
s7 = s5.index("a", 8, -1)
print(s6)
print(s7)
print("#"*20)
print("*"*20)


# count()  计算字符串出现的次数
s5 = "akjksdsaaa"
print(s5.count("a"))
print(s5.count("a", 2, 10))
print(s5.count("a", 2, -1))  # -1的a不包括,就会出现2次a
print("*"*20)

# startswith() 检测是否以指定字母开头,返回布尔值
# endswith() 检测是否以指定字母结束,返回布尔值
k = "l like dog"
print(k.startswith("l",-2, -1))
print(k.startswith(("i")))
print(k.startswith(("l")))
print(k.endswith("g"))
print("*"*20)

# isupper() 检测所有字母是否大写字母,返回布尔值
k_upper = "KKK"
k_lower = "ppo"
print(k_upper.isupper())
print(k_lower.isupper())
print("*"*20)

# islower 检测所以字母是否是小写,返回布尔值
print(k_upper.islower())
print(k_lower.islower())
print("*"*20)

# istitle() 检测是否以指定标题显示(每个单词首字母大写),返回布尔值
print(k_upper.istitle())
print(k_lower.istitle())
k2 = "I Like Dog"
print(k2.istitle())
print("*"*20)

# issapce() 检测字符串是否是空字符串 (至少有一个,否则返回False)
k3 = "    "
k4 = "   l"
print(k3.isspace())
print(k4.isspace())
print("*"*20)

# isalpha() 检测字符串是否是字母组成,返回布尔值
p = "l都dog"
print(p.isalpha())
p1 = "l 都dog"
print(p1.isalpha())
print("*"*20)

# isalnum() 检测字符串是否有字母加数字组成,返回布尔值
p = "l都dog122"
print(p.isalnum())
p1 = "l 都dog112"
print(p1.isalnum())
p2 = "122"
print(p2.isalnum())
p3 = "kk"
print(p3.isalnum())
print("*"*20)

# isdigit()
# isdecimal()
# isnumeric()
"""
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节）
False：汉字数字，罗马数字，小数
Error：无

isdecimal()
True: Unicode数字，全角数字（双字节）
False：罗马数字，汉字数字，小数
Error:byte数字（单字节）isnumeric（）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False：小数
Error；byte数字（单字节）
"""
s5 = "123"
print(s5.isdigit())
print(s5.isdecimal())
print(s5.isnumeric())
print()
print("*"*20)

s8 = b"101100"
print(s8.isdigit())
# print(s8.isdecimal())
# print(s8.isnumeric())
print()
print("*"*20)

s7 = "12.002"
print(s7.isdigit())
print(s7.isdecimal())
print(s7.isnumeric())
print()
print("*"*20)


s8 = "三叁"
print(s8.isdigit())
print(s8.isdecimal())
print(s8.isnumeric())
print()
print("*"*20)

s9 = "Ⅲ"
print(s9.isdigit())
print(s9.isdecimal())
print(s9.isnumeric())
print()
print("*"*20)


# split() 用指定字符切割字符串  返回有字符串组成的列表
u = "日照香炉生紫烟*疑是银河落九天"
u2 = u.split("*")
print(u2)
print("*"*20)

# splitlines() 以换行切割字符串
u4 = "日照香炉生紫烟\n\n疑是银河落九天"
u3 = u4.splitlines()
print(u3)
print("*"*20)

# join() 将列表按照指定字符串连接  返回字符串
list1 = ["日照香炉生紫烟", "疑是银河落九天"]
s10 = "#".join(list1)
print(s10)
print("*"*20)

# ljust() 指定字符串的长度,内容靠左边,不足的位置用指定字符填充,默认空格,返回字符串
s11 = "oopo"
print(len(s11))
print(s11.ljust(7, "."))
print("*"*20)

# center() 指定字符串的长度,内容居中,不足的位置用指定字符填充,默认空格,返回字符串
s12 = "oopop"
print(len(s12))
print(s12.center(8, "."))
print("*"*20)

# rjust() 指定字符串的长度,内容靠右,不足的位置用指定字符填充,默认空格,返回字符串
s12 = "oopop"
print(len(s12))
print(s12.rjust(8, "."))
print("*"*20)

# strip() 去掉左右两边指定字符,默认空格
s13 = "  a12  "
print("--" + s13 + "--")
print("--" + s13.strip() + "--")
print("*"*20)

# lstrip() 去掉左侧指定字符,默认空格
s14 = "   a12  "
print("--" + s13 + "--")
print("--" + s13.lstrip() + "--")
print(s13.lstrip("a"))
print(s13.lstrip(" a"))
print("*"*20)

# rstrip() 去掉右侧指定字符,默认空格
s14 = "  a12  "
print("--" + s13 + "--")
print("--" + s13.rstrip() + "--")
print(s14.rstrip("2"))
print(s14.rstrip("2 "))
print("*"*20)

# zfill()  指定字符串长度,内容靠右边,不足的位置用0填充
s15 = "abc"
print(s15.zfill(7))
print("*"*20)

# maketrans() 生成用于字符串替换的映射表
# translate() 进行字符串替换
s16 = "abcdefg"
s17 = s16.maketrans("c","M")
print(s16)
print(s17)
print(s16.translate(s17))
print("*"*20)
