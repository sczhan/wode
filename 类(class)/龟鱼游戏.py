#
# class Ticket(object):
#     """"
#     票价
#     """
#     def __init__(self, weekend=False, child=False):
#         self.exp = 100
#         if weekend:
#             self.inx = 1.2
#         else:
#             self.inx = 1
#
#         if child:
#             self.dis = 0.5
#         else:
#             self.dis = 1
#
#     def cal_people(self, num):
#         """
#         计算票价
#         :param num: 人数
#         :return: 总共的票价
#         """
#         return self.exp * self.inx * self.dis * num
#
#
# aduit = Ticket(weekend=True)
# child = Ticket(child=True)
# print("两个成年人,一个小孩子在周末的价格{0}元".format(int(aduit.cal_people(2) + child.cal_people(1))))
#
#
# import math
#
#
# class Point(object):
#     """
#     点
#     """
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_x(self):
#         """
#         x 坐标
#         :return:x坐标
#         """
#         return self.x
#
#     def get_y(self):
#         """
#         y坐标
#         :return:y坐标
#         """
#         return self.y
#
#
# L1 = Point(2, 3)
# L2 = Point(5, 7)
#
#
# class Line(object):
#     """
#     直线类
#     """
#     def __init__(self, k1, k2):
#         self.x = k1.get_x() - k2.get_x()
#         self.y = k1.get_y() - k2.get_y()
#         self.len = math.sqrt(self.x*self.x + self.y*self.y)
#
#     def jilu(self):
#         """
#         两点之间的距离
#         :return: 距离
#         """
#         return self.len
#
#
# l = Line(L1, L2)
# print(l.jilu())


import random


class Turtle(object):
    """
    龟
    移动可以选择1或者2  范围是0 <= x <= 10 0 <= y <= 10
    如果移动到边缘,自动反方向移动
    每次移动消耗体力100
    体力上限为100,消耗完则游戏结束
    如果
    """
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.power = 100

    def move(self):
        new_x = random.choice([1, 2, -1, -2]) + self.x
        new_y = random.choice([1, 2, -1, -2]) + self.y
        self.power -= 1

        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - new_x
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_x > 10:
            self.y = 10 - new_y
        else:
            self.y = new_y

        return self.x, self.y

    def eat(self):
        self.power += 20
        if self.power >= 100:
            self.power = 100


class Fish(object):
    """
    鱼
    10条 ,每次移动1,不消耗体力  范围是0 <= x <= 10 0 <= y <= 10
    如果移动到边缘,自动反方向移动
    被龟吃完游戏结束
    """
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        new_x = random.choice([1, -1]) + self.x
        new_y = random.choice([1, -1]) + self.y

        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - new_x
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_x > 10:
            self.y = 10 - new_y
        else:
            self.y = new_y

        return self.x, self.y


turtle = Turtle()
fish = []
for i in range(10):
    each_fish = Fish()
    fish.append(each_fish)

a = 0
while True:
    if not len(fish):
        print("鱼被吃完了")
        break

    if not turtle.power:
        print("乌龟,体力消耗完了")
        break

    pos = turtle.move()

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            a += 1
            print("有{}条鱼被吃了".format(a))
            turtle.eat()
            fish.remove(each_fish)