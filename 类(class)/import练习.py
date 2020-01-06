import random
# x = random.randint(100, 999)
# n = 10
# while n:
#     # 输入函数
#     num = input("请输入一个三位数")
#     # 检测输入是否是纯数字
#     if num.isdigit():
#         # 输入函数的是字符类型,不强制会报错
#         num = int(num)
#         if 100 <= num <= 999:  # if 100<= int(num) <= 999:
#             """判断输入的数与系统随机数比较大小
#             """
#             if x > num:
#                 print("数字太小了\n")
#                 n -= 1
#             elif x == num:
#                 print("你猜对了")
#                 print(x)
#                 print(math.pow(x, 2))  # 打印出x的平方
#                 break
#             else:
#                 print("数字太大了\n")
#                 n -= 1
#
#         else:
#             print("请按规定输入三位数")
#     else:
#         print("请按规定输入")
#
# print("正确答案:" + str(x))


'''
输入一个三位数与程序随机数比较大小
如果大于程序随机数,则分别输出这个三位数的个位  十位 百位
如果等于程序随机数,则提示中奖,记100分
如果小于程序随机数,则将120个字符输入到文本文件中
    (规则是每一条字符串的长度为12,单独占一行,并且前4个是字母,后8个是数字)
'''


# def save():
#     """
#     :return: str_num
#     """
#     # 定义一个空字符串用于拼接字符
#     str_num = ""
#     # 循环前四个随机字母(用ascii对应的值来随机在转换为字母)
#     for i in range(0, 4):
#         # 随机小写的ascii值
#         sjshuzi = random.randrange(97, 123)
#         # 将ASCII值转换成对应的字母
#         zimu = chr(sjshuzi)
#         # 依次拼接得到的随机字母
#         str_num += zimu
#     # print(str_num)
#     # 循环后八个随机数字
#     for i in range(8):
#         num = random.randrange(0, 10)
#         str_num += str(num)
#     return str_num
#
#
# # 定义一个变量用于存取初始分数
# source = 0
# # 定义一个变量用于累计输入了多少次
# cishu = 0
#
#
# def num_game():
#     global source
#     global cishu
#     while 1:
#         # 输入函数
#         num = input("请输入一个三位数,输入-1结束:")
#         # 程序随机数
#         if num == "-1":
#             break
#         sjs = random.randrange(100, 1000)
#         # 检测输入是否是纯数字
#         if num.isdigit() and 100 <= int(num) <= 999:  # 输入函数返回的是字符类型,不能与整形直接比较,需要强制类型转换
#             # 计算输入多少次
#             cishu += 1
#             num = int(num)
#             sjs = int(sjs)
#             print("你输入%d次" % cishu)
#             if num > sjs:
#                 # 求百位数字方法(地板除100或用数字模块当中的floor()函数
#                 bai = num // 100
#                 # 求十位数的方法是先把三位数数字去100的余数,在地板除10
#                 shi = (num % 100)//10
#                 # 求个位数的方法是直接去10的余
#                 ge = num % 10
#                 print("你输入的这个数太大了,程序随机是:", sjs)
#                 print("这个三位数的个位数是{0},十位数{1},百位数{2}" .format(ge, shi, bai))
#             if num == sjs:
#                 # 所得分数
#                 source += 100  # source = source +100
#                 print("你猜对了", sjs)
#                 print("当前积分为:", str(source))
#                 print("你中奖的概率是多少", source/cishu)
#             if num < sjs:
#                 print("你输入的数比程序随机数小,程序随机数是:", sjs)
#             # 有120个字符每行12个可知只需存入10行就行
#                 for i in range(10):
#                     str_line = save()
#                     # print(str_line)
#                     # 执行文件存入操作
#                     with open("F:\\str_num.txt", 'a') as f:
#                         f.write(str_line+"\n")
#         else:
#             print("请按规定输入")
#
#
# # 程序入口
# if __name__ == "__main__":  # 模块包 (调试代码)
#     print(__name__)  # 在本身模块中__name__ == __main__ ,当第三方导入的时候 __name__ == 文件名
#     num_game()


"""
def num_game(source, cishu): 
    while 1:
        # 输入函数
        num = input("请输入一个三位数,输入-1结束:")
        # 程序随机数
        if num == "-1":
            break
        sjs = random.randrange(100, 1000)
        # 检测输入是否是纯数字
        if num.isdigit() and 100 <= int(num) <= 999:  # 输入函数返回的是字符类型,不能与整形直接比较,需要强制类型转换
            # 计算输入多少次
            cishu += 1
            num = int(num)
            sjs = int(sjs)
            print("你输入%d次" % cishu)
            if num > sjs:
                # 求百位数字方法(地板除100或用数字模块当中的floor()函数
                bai = num // 100
                # 求十位数的方法是先把三位数数字去100的余数,在地板除10
                shi = (num % 100)//10
                # 求个位数的方法是直接去10的余
                ge = num % 10
                print("你输入的这个数太大了,程序随机是:", sjs)
                print("这个三位数的个位数是{0},十位数{1},百位数{2}" .format(ge, shi, bai))
            if num == sjs:
                # 所得分数
                source += 100  # source = source +100
                print("你猜对了", sjs)
                print("当前积分为:", str(source))
                print("你中奖的概率是多少", source/cishu)
            if num < sjs:
                print("你输入的数比程序随机数小,程序随机数是:", sjs)
            # 有120个字符每行12个可知只需存入10行就行
                for i in range(10):
                    str_line = save()
                    # print(str_line)
                    # 执行文件存入操作
                    with open("F:\\str_num.txt", 'a') as f:
                        f.write(str_line+"\n")
        else:
            print("请按规定输入")


# 程序入口
if __name__ == "__main__":  # 模块包
    # 定义一个变量用于存取初始分数
    source = 0
    # 定义一个变量用于累计输入了多少次
    cishu = 0
    num_game(source, cishu)
"""


class GameNum(object):

    def save(self):
        """
        :return: str_num
        """
        # 定义一个空字符串用于拼接字符
        str_num = ""
        # 循环前四个随机字母(用ascii对应的值来随机在转换为字母)
        for i in range(0, 4):
            # 随机小写的ascii值
            sjshuzi = random.randrange(97, 123)
            # 将ASCII值转换成对应的字母
            zimu = chr(sjshuzi)
            # 依次拼接得到的随机字母
            str_num += zimu
        # print(str_num)
        # 循环后八个随机数字
        for i in range(8):
            num = random.randrange(0, 10)
            str_num += str(num)
        return str_num

    def num_game(self, source, cishu):
        while 1:
            # 输入函数
            num = input("请输入一个三位数,输入-1结束:")
            # 程序随机数
            if num == "-1":
                break
            sjs = random.randrange(100, 1000)
            # 检测输入是否是纯数字
            if num.isdigit() and 100 <= int(num) <= 999:  # 输入函数返回的是字符类型,不能与整形直接比较,需要强制类型转换
                # 计算输入多少次
                cishu += 1
                num = int(num)
                sjs = int(sjs)
                print("你输入%d次" % cishu)
                if num > sjs:
                    # 求百位数字方法(地板除100或用数字模块当中的floor()函数
                    bai = num // 100
                    # 求十位数的方法是先把三位数数字去100的余数,在地板除10
                    shi = (num % 100)//10
                    # 求个位数的方法是直接去10的余
                    ge = num % 10
                    print("你输入的这个数太大了,程序随机是:", sjs)
                    print("这个三位数的个位数是{0},十位数{1},百位数{2}" .format(ge, shi, bai))
                if num == sjs:
                    # 所得分数
                    source += 100  # source = source +100
                    print("你猜对了", sjs)
                    print("当前积分为:", str(source))
                    print("你中奖的概率是多少", source/cishu)
                if num < sjs:
                    print("你输入的数比程序随机数小,程序随机数是:", sjs)
                    # 有120个字符每行12个可知只需存入10行就行
                    for i in range(10):
                        str_line = GameNum.save(self)
                        # print(str_line)
                        # 执行文件存入操作
                        with open("F:\\str_num.txt", 'a') as f:
                            f.write(str_line+"\n")
            else:
                print("请按规定输入")


# 程序入口
if __name__ == "__main__":  # 模块包
    # 定义一个变量用于存取初始分数
    source = 0
    # 定义一个变量用于累计输入了多少次
    cishu = 0
    # num_game(source, cishu)


# a = GameNum()
# a.num_game(source, cishu)

