# print("=_=|||")
#
# import turtle
# turtle.setup(650,350,200,200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor('purple')
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40,80)
#     turtle.circle(-40,80)
# turtle.circle(40,80/2)
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40*2/3)
# turtle.done()
#
#
# company = "北京课工场教育科技有限公司"
# name = "张丽"
# job = "课程设计师"
# iphone = "138111111"
# tel = "010-12345678"
# city = "北京市海淀区成府路207号"
# print(company)
# print(name + "   " + job)
# print("手机: " + iphone)
# print("电话: " + tel)
# print("地址: " + city)

# 变量weather_case记录天气情况
# 晴天或多云时，
# weather_case=True
# weather = input("请输入周末的天气情况(晴天\下雨\阴天\多云): ")
# print("-----周末计划表-----")
# weather_case = (weather == '晴天'or weather == '多云')
# print("天气情况     外出游玩")
# print(weather + "\t\t" + str(weather_case))

# huashidu = input("请输入华氏度: ")
# sheshidu = 5/9.0 * (float(huashidu)-32)
# print("华氏温度\t\t摄氏温度")
# print(huashidu + "\t\t\t" + str(int(sheshidu)))

#
# word1 = "   when I WasYoung i'd listen to the Radio   "
# word2 = "   waiting for My Favorite songs     "
# word3 = "   when They played i'd sing Along   "
# word4 = "   it Made me Smile  "
# print(word1.strip().capitalize().replace("i", "I", 1))
# print(word2.strip().capitalize())
# print(word3.strip().capitalize())
# print(word4.strip().capitalize())

# word1 = "   haPPy BiRthDAy To u"
# word2 = "Happy biRthDAy To you"
# word3 = " haPpy BirThdAy 2 deAr LiLi"
# word4 = " happy birthday 2 u"
# print(word1.strip().lower().replace("u", "you"))
# print(word2.strip().lower().replace("u", "you"))
# print(word3.strip().lower().replace("2", "to"))
# print(word4.strip().lower().replace("u", "you").replace("2", "to"))

# str1 = "My name is Limin"
# print(str1.lower())
# print(str1[8:13])
# str2 = str1.replace("imin", "ilei")
# print(str2)

# near = input("请大地主输入拥有的田地(亩): ")
# print("-------田地面积-------")
# pifang = int(near) * 666.67
# print("亩     平方米")
# print("%s      %d" % (near, pifang))

# number = []
# number1 = input("请输入第1个整数: ")
# number2 = input("请输入第2个整数: ")
# number3 = input("请输入第3个整数: ")
# number4 = input("请输入第4个整数: ")
# number5 = input("请输入第5个整数: ")
# number6 = input("请输入第6个整数: ")
# number.append(number1)
# number.append(number2)
# number.append(number3)
# number.append(number4)
# number.append(number5)
# number.append(number6)
#
# for i in range(0, len(number)):
#     for j in range(0, len(number) - i - 1):
#         if int(number[j]) > int(number[j+1]):
#             number[j],  number[j+1] = number[j+1],  number[j]
#
# print(number)

#
# song = "Twinkle,twinkle,little star," \
#        "How I wonder what you are!" \
#        "Up above the world so high," \
#        "Like a diamond in the sky." \
#        "Twinkle,twinkle,little star," \
#        "How I wonder what you are!" \
#        "When the blazing sun is gone," \
#        "When he nothing shines upon," \
#        "Then you show your little light," \
#        "Twinkle,twinkle,all the night"
#
# songs = song.lower().replace(",", " ").replace("!", " ").replace(".", " ").split(" ")
# dict = {}
# print(songs)
# for i in songs:
#     if i in dict.keys():
#         dict[i] += 1
#     else:
#         dict[i] = 1
#
# dict_sort = sorted(dict.items(), key=lambda k: k[1], reverse=True)
# print(dict_sort)
# for key in dict_sort:
#     print(key[0], key[1])

import time


def weilai_time(times):
    t = time.time() + times * 3600
    print(time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(t)))


weilai_time(1)