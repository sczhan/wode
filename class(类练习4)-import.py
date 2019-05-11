import import练习
import class_类练习_04_zimu_game


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
    a.num_game(0, 0, 100)
elif game == "2":
    mm = input("请输入字母: ")
    b = class_类练习_04_zimu_game.Game_zimu()
    getattr(b, mm)()   # getattr()通过字符串调用同名函数


else:
    print("退出")

