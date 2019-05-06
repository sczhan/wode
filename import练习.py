
import math
import random
x = random.randint(100, 999)
n = 10
while n:
    # 输入函数
    num = input("请输入一个三位数")
    # 检测输入是否是纯数字
    if num.isdigit():
        # 输入函数的是字符类型,不强制会报错
        num = int(num)
        if 100 <= num <= 999:  # if 100<= int(num) <= 999:
            """判断输入的数与系统随机数比较大小
            """
            if x > num:
                print("数字太小了\n")
                n -= 1
            elif x == num:
                print("你猜对了")
                print(x)
                print(math.pow(x, 2))  # 打印出x的平方
                break
            else:
                print("数字太大了\n")
                n -= 1

        else:
            print("请按规定输入三位数")
    else:
        print("请按规定输入")

print("正确答案:" + str(x))