# print("\"")
# temp = input("请输入数字: ")
# if temp.isdigit():
#     temp = int(temp)
#     if 1<=temp<=100:
#         print('1')
#     else:
#         print("11丑八怪")
# else:
#     print("丑八怪")
year = input("请输入年份: ")
if year.isdigit():
    year = int(year)
    if year % 4 ==0:
        print(str(year)+"是闰年")
    else:
        print(str(year)+"不是闰年")
else:
    print("输入年份")
import random
secert = random.randint(1, 100)
times = 3
while times:
    num = input("请输入数字")
    if num.isdigit():
        a = int(num)
        if a == secert:
            print("你才对了")
            break
        elif a < secert:
            print("你猜的数字太小了")
            times = times - 1
        else:
            print("数字太大了")
            times = times - 1
    else:
        print("输入数字")
print(secert)
print(secert)
print(secert)
print(secert)
print(secert)
print(secert)