
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

# [: :] 字符串的切片操作
# [开始索引:结束索引:间隔值] (包含开始,不包含结束)
print(s3[2:6])
print(s3[-8:-4:1])
print(s3[-2:-6:-1])
# 切整个字符串
print(s3[:])
# 指定开始,不指定结束
print(s3[2:])
# 指定结束,不指定开始
print(s3[:6])
# 指定开始,不指定结束并给出间隔值
print(s3[2::2])
# 指定结束,不指定开始并给出间隔值
print(s3[:6:3])

# capitalize() 首字母大写 返回字符串
s = "i love you"
print(s.capitalize())


# title() 每个单词的首字母大写 返回字符串
print(s.title())

# upper() 将所有字母大写 返回字符串
print(s.upper())

# lower() 将所有字母小写  返回字符串
print(s.lower())

# swapcase() 大小写互换  返回字符串
s4 = "L Ll"
print(s4.swapcase())

# len() 计算字符串长度,不属于字符串的内建函数
print(len(s4))

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

# count()  计算字符串出现的次数
s5 = "akjksdsaaa"
print(s5.count("a"))
print(s5.count("a", 2, 10))
print(s5.count("a", 2, -1)) # -1的a不包括,就会出现2次a
