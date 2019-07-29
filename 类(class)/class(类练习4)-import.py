import class_类练习_04_zimu_game
import import练习

# class zimu(class_类练习_04_zimu_game.Game_zimu):
#     def __init__(self, a):
#         c = class_类练习_04_zimu_game.Game_zimu()
#         self.a = c.a()
#         # self.b = c.b()
#         # self.c = c.c()
#
#
# zimu_a = zimu("a")
#
#
# class Game(zimu):
#     def __init__(self, zimus):
#         super.__init__(zimus)
#         print("请选择游戏:\n 1.数字游戏: \n 2.字母游戏")
#         game = input("请输入1或者2: ")
#         mm = input("请输入字母")
#
#     def shuzi(self):
#         a = import练习.GameNum()
#         a.num_game(0, 0, 100)
#
#     def zimu(self, ms):
#         self.ms = mm
#         b = class_类练习_04_zimu_game.Game_zimu
#         b.zimus(mm)
#
#
#
# av = Game()
# av.zimu(a)


'''
     print("请选择游戏:\n 1.数字游戏: \n 2.字母游戏")
        game = input("请输入1或者2: ")
        if game == "1":
            a = import练习.GameNum()
            a.num_game(0, 0, 100)
        elif game == "2":
            mm= input("请输入字母: ")
            b = class_类练习_04_zimu_game.Game_zimu
            if mm == "a":
            b.a()
        else:
            print("退出")
'''


print("请选择游戏:\n 1.数字游戏: \n 2.字母游戏")
game = input("请输入1或者2: ")
if game == "1":
    a = import练习.GameNum()
    a.num_game(0, 0)
elif game == "2":
    while True:
        mm = input("请输入字母或者任意数字退出: ")
        if mm.isdigit():
            break
        else:
            b = class_类练习_04_zimu_game.Game_zimu()

            # 方法1  getattr() 是 python 的内建函数，getattr(object,name) 就相当于 object.name，但是这里 name 可以为变量。
            getattr(b, mm)()   # getattr()通过字符串调用同名函数

    # 方法2
    # from operator import methodcaller
    # methodcaller(mm)(b)

    #  下面三个适合用于没有class 只有函数
    # def a():
    #     for i in range(5):
    #         # 判断开始输入的位置
    #         for j in range(4 - i):
    #             print(" ", end="")
    #         # 控制行
    #         for j in range(i + 1):
    #             if i == 0 or i == 2:
    #                 print("* ", end="")
    #                 continue
    #             if j == i or j == 0:
    #                 print("* ", end="")
    #                 continue
    #             else:
    #                 print("  ", end="")
    #         print()
    # eval(mm)()

    # globals()[mm]()

    # locals()[mm]()


else:
    print("退出")


