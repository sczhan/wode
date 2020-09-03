month = int(input("请输入您出行的月份(1~12）："))
plane = int(input("请问您选择头等舱还是经济舱(头等舱输入1，经济舱输入2)："))
money = 5000
if 4 <= month <= 10 and plane == 1:
    print("您的机票价格为：", money * 0.9)
elif 4 <= month <= 10 and plane == 2:
    print("您的机票价格为：", money * 0.6)
elif month <= 3 or month >= 11 and plane == 1:
    print("您的机票价格为：", money * 0.5)
elif month <= 3 or month >= 11 and plane == 2:
    print("您的机票价格为：", money * 0.4)


while True:
    n = int(input("请输入数字1~7(输入0结束)："))
    if n == 0:
        print("程序结束")
        break
    day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    print(day_list[n-1])


x = input("输入一个整数：")
count = 0
list = []
while count < len(x):
    list.append(x[-(1+count)])
    count += 1
print("反转后的结果为："+"".join(list))