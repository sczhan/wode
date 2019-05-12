
# Tkinter项目-屏保
# 项目分析:
# 1.屏保可以自己启动,也可以手动启动
# 2.一旦敲击键盘或者移动鼠标后,或者其他的引发时间,则停止
# 3.如果屏保是一幅画的话,则没有画框
# 4.图像的动作是随机的具有随机性,可能包括颜色,大小,多少,运动方向,变形等

# 整个世界构成
# 1.ScreenSaver: 屏保
#      - 需要一个canvas,大小与屏幕一致,没有边框
# 2. Ball:球
#      - 颜色,大小,多少,运动方向,变形等随机
#      - 球能动,可以被调用
import random
import tkinter

class Ball(object):
    """
    定义运动的球的类
    """
    def __init__(self, canvas, scrnwidth, scrnheight):
        """
        :param canvas: 画布  所有内容都应该在画布上呈现出来,此处通过变量传入
        :param scrnwidth: 屏幕的宽
        :param scrnheight: 屏幕的高
        """
        # 球出现的初始位置要随机,此位置表示的球的圆心
        # xpos表示位置的x坐标
        self.xpos = random.randint(10, int(scrnwidth)-20)
        # ypos表示位置的y坐标
        self.ypos = random.randint(30, int(scrnheight)-10)

        # 定义球运动的速度
        # 模拟运动 不断的擦掉原来的画,然后在一个新的地方再从新绘制
        # 此处xvelocity模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        # 同理,yvelocity模拟的是y轴方向运动
        self.yvelocity = random.randint(3, 15)

        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        # 定义屏幕的高度
        self.scrnheight = scrnheight

        # 球的大小随机
        # 此处球的大小用半径表示
        self.radius = random.randint(20, 120)

        # 定义颜色
        # RGB表示法:三个数字,每个数字的值是0-255之间,表示红禄蓝三个颜色的大小
        # 在某些系统中, 之间用英文单词表表示也可以,比如red, green
        # 此处用lambda表达式
        c = lambda: random.randint(0, 255)
        self.color = "#%02x%02x%02%" % (c(), c(), c())

        def create_ball(self):
            """
            用构造函数定义的变量值, 在canvas上画一个球
            :param self:
            :return:
            """
            # tkinter没有画圆形函数
            # 只要一个花椭圆函数,花椭圆需要定义两个坐标,
            # 在一个长方形内画椭圆,我们只需要定义长方形左上角和右下角就好
            # 求两个坐标的方法是, 已知圆心的坐标,则圆心坐标减去半径能求出左上角,加上半径能求出右下角坐标
            x1 = self.xpos - self.radius
            # 继续球y1, x2, y2
            y1 = self.ypos - self.radius
            x2 = self.xpos + self.radius
            y2 = self.ypos + self.radius

            # 再有两个对角坐标的前提下,可以进行画圆
            # fill 表示填充颜色
            # outline是外围边框颜色
            self.item = self.canvas.create_oval(x1, y1, x2, y2,\
                                                fill=self.color,\
                                                outline=self.color)


class ScreenSaver():
    """
    定义屏保的类
    可以被启动
    """
    pass
