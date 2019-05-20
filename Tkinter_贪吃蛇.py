
# 项目分析
#  构成:
#       蛇 Snake
#       食物 Food
#       世界 World
#  蛇和食物属于整个世界
#           class  World:
#                   self.snake
#                   self.food
#          上面代码不友好
#          我们用另外一个思路来分析

# 我们的分析思路
#       食物是一个独立的事物
#       蛇也可以是认为一个独立的事物
#       世界也是,但世界负责显示

import random
import threading


class Food(object):

    """
    功能:
        1.出现在画面的某一个地方
        2.一旦被吃,则增加蛇的分数
    """
    def __init__(self, queue):
        """
        自动产生一个食物
        """
        self.queue = queue
        self.new_food()

    def new_food(self,):
        """
        功能:产生一个食物
        产生一个食物的过程就是随机产生一个食物坐标的过程
        :return: None
        """
        # 注意横纵坐标产生的范围
        x = random.randrange(50, 480, 10)
        # 同理产生y坐标
        # 需要注意的是, 我们正给游戏屏幕一般不需要把他设置成正方形
        y = random.randrange(50, 480, 10)
        self.position= x, y   # position存放食物位置

        # 队列, 就是一个不能够访问内部元素,只能从头弹出一个元素并只能从队尾追加元素list
        # 把一个食物产生的消息放入队列
        # 消息的格式,自己定义
        # 我的定义是: 消息是一个dict, k代表消息类型,v代表此类型的数据
        self.queue.put({"food": self.position})


class Snake(threading.Thread):
    """
    蛇的功能:
        1. 蛇能动,由我们上下左右按键控制
        2. 蛇每次动, 都需要重新计算蛇头的位置
        3. 检测是否游戏完事的功能
    """
    def __init__(self, world, queue):
        threading.Thread.__init__(self)
        self.world = world
        self.queue
        self.points_earned = 0  # 游戏分数
        self.food = Food(self.queue)
        self.snake_points = [(495, 55), (485, 55), (475, 55), (465, 55)]

        self.start()

    def run(self):
        """
        一旦启动多线程调用此函数
        要求蛇一直都在跑
        :return:
        """
        if self.world.is_game_over:
            self.delete()
        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            self.time.sleep(0.5)  # 控制蛇的速度
            self.move()

    def move(self):
        """
        负责蛇的移动
            1. 重新计算蛇头的坐标
            2. 当蛇头跟食物相遇,则加分,重新生成食物,通知world,加分
            3. 否则,蛇需要动
        :return: None
        """
        new_snake_point = self.cal_new_pos()  # 重新计算蛇头位置

        # 蛇头位置跟食物位置相同
        if self.food.position == new_snake_point:
            self.points_earned += 1  # 得分加1
            self.queue.put({"points_earned": self.points_rarned})
            self.food.new_food()
        else:
            """
            需要注意蛇的信息的保存方式
            每次移动是删除存放蛇最前位置,并在后面追加
            """
            self.snake.points.pop(0)
            # 判断程序是否退出,因为新的蛇可能撞墙
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)

    def cal_new_position(self):
        """
        计算新的 蛇头位置
        :return: new_snake_point
        """
        last_x, last_y = self.snake_points[-1]
        if self.direction == "Up":  # direction负责存储蛇移动的方向
            new_snake_point = last_x, last_y - 10  # 每次移动的跨度是10像素
        elif self.direction == "Donw":
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Left":
            new_snake_point = last_x - 10 , last_y
        elif self.direction == "Right":
            new_snake_point = last_x +10, last_y

        return new_snake_point

    def key_pressed(self, e):
        """
        keysym 是按键名称
        :param e: 
        :return: None
        """
        self.direction = e.keysym2

    def check_game_over(self, snake_point):
        """
        判断的依据是蛇头是否和墙相撞
        :param snake_point:
        :return:
        """
        # 把蛇头的坐标拿出来,跟墙的坐标进行判断
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({"game_over": True})


