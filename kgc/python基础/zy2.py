
word1 = "   haPPy BiRthDAy To u"
word2 = "Happy biRthDAy To you"
word3 = " haPpy BirThdAy 2 deAr LiLi"
word4 = " happy birthday 2 u"
print(word1.strip().lower().replace("u", "you"))
print(word2.strip().lower().replace("u", "you"))
print(word3.strip().lower().replace("2", "to"))
print(word4.strip().lower().replace("u", "you").replace("2", "to"))

str1 = "My name is Limin"
print(str1.lower())
print(str1[8:13])
str2 = str1.replace("imin", "ilei")
print(str2)

near = input("请大地主输入拥有的田地(亩): ")
print("-------田地面积-------")
pifang = int(near) * 666.67
print("亩     平方米")
print("%s      %d" % (near, pifang))
