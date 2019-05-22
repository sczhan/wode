
class Ticket(object):
    """"
    票价
    """
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inx = 1.2
        else:
            self.inx = 1

        if child:
            self.dis = 0.5
        else:
            self.dis = 1

    def cal_people(self, num):
        """
        计算票价
        :param num: 人数
        :return: 总共的票价
        """
        return self.exp * self.inx * self.dis * num


aduit = Ticket(weekend=True)
child = Ticket(child=True)
print("两个成年人,一个小孩子在周末的价格{0}元".format(int(aduit.cal_people(2) + child.cal_people(1))))


import math


class Point(object):
    """
    点
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        """
        x 坐标
        :return:x坐标
        """
        return self.x

    def get_y(self):
        """
        y坐标
        :return:y坐标
        """
        return self.y


L1 = Point(2, 3)
L2 = Point(5, 7)


class Line(object):
    """
    直线类
    """
    def __init__(self, k1, k2):
        self.x = k1.get_x() - k2.get_x()
        self.y = k1.get_y() - k2.get_y()
        self.len = math.sqrt(self.x*self.x + self.y*self.y)

    def jilu(self):
        """
        两点之间的距离
        :return: 距离
        """
        return self.len


l = Line(L1, L2)
print(l.jilu())