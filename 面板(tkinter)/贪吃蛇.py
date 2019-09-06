import queue
import random
import threading
import time
from tkinter import *


class Food(object):
    """
    1,出现在画面的某一个地方
    """
    def __init__(self, queue):
        self.queue = queue
        self.new_food()

    def new_food(self):
        """
        产生一个食物的过程,随机产生一个食物坐标的过程
        postion:食物的坐标
        :return: None
        """
        x = random.randrange(55, 480, 10)
        y = random.randrange(45, 280, 10)
        # postion 用来存放食物的位置(坐标)
        self.postion = x, y
        self.ep = x -5 , y - 5, x + 5, y + 5
        self.queue.put({"food": self.ep})


class Snake(threading.Thread):
        """
        1.蛇能动,由我们上下左右键控制
        2.蛇每次动,都需要重新计算蛇头的位置
        3.检测是否游戏完事的功能
        """
        def __init__(self, queue, world):
            threading.Thread.__init__(self)
            self.queue = queue
            self.world = world
            self.points_earned = 0
            self.food = Food(queue)
            self.snake_points = [(485, 55), (475, 55), (465, 55), (455, 55)]
            self.daemon = True
            self.direction = "Left"
            self.start()

        def run(self):
            """
            多线程必须启动的run函数
            """
            if self.world.is_game_over:
                self._delete()

            while not self.world.is_game_over:
                self.queue.put({"move": self.snake_points})
                time.sleep(0.1)
                self.move()

        def key_pressed(self, e):
            """
            绑定按键
            :param e:
            :return:
            """
            self.direction = e.keysym

        def move(self):
            """
            控制蛇的移动
            :return: new_snake_point
            """
            new_snake_point = self.cal_new_snake()
            if self.food.postion == new_snake_point:
                self.points_earned += 1
                self.queue.put({"points_earned": self.points_earned})
                self.food.new_food()
            else:
                self.snake_points.pop(0)
                self.check_game_over(new_snake_point)
                self.snake_points.append(new_snake_point)

        def cal_new_snake(self):
            """
            蛇头
            :return:new_snake_point
            """
            last_x, last_y = self.snake_points[-1]
            if self.direction == "Up":
                new_snake_point = last_x, last_y - 10
            elif self.direction == "Down":
                new_snake_point = last_x, last_y + 10
            elif self.direction == "Left":
                new_snake_point = last_x - 10, last_y
            elif self.direction == "Right":
                new_snake_point = last_x + 10, last_y

            return new_snake_point

        def check_game_over(self, snake_point):
            """
            游戏结束
            :return:
            """
            x, y = snake_point[0], snake_point[1]
            if not -1 < y < 301 or not -1 < x < 500 or snake_point in self.snake_points:
                self.queue.put({"game_over": True})


class World(Tk):
    """
    用来模拟整个游戏画板
    """
    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False

        self.canvas = Canvas(self, width=500, height=300, bg="white")
        self.canvas.pack()
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill="blue", outline="blue")
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill="green", width=10)
        self.points_earned = self.canvas.create_text(450, 20, fill="yellow", text="Score: 0")
        self.queue_han()

    def queue_han(self):
        """"
        """
        try:
            while True:
                task = self.queue.get(block=False)
                if task.get("move"):
                    points = [x for point in task["move"] for x in point]
                    self.canvas.coords(self.snake, *points)
                if task.get("food"):
                    self.canvas.coords(self.food, *task["food"])
                if task.get("game_over"):
                    self.game_over()
                elif task.get("points_earned"):
                    self.canvas.itemconfigure(self.points_earned, text="Score :{}".format(task["points_earned"]))
                    self.queue.task_done()

        except queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_han)

    def game_over(self):
        """
        游戏结束
        :return:
        """
        self.is_game_over = True
        self.canvas.create_text(200, 150, fill="yellow", text="Game Over")
        qb = Button(self, text="Quit", command=self.destroy)
        rb = Button(self, text="Begin", command=self.__init__)
        self.canvas.create_window(200, 180, anchor='nw', window=qb)
        self.canvas.create_window(150, 180, anchor="nw", window=rb)


if __name__ == "__main__":
    q = queue.Queue()
    world = World(q)
    snake = Snake(q, world)
    world.title("贪吃蛇")
    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Up>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)
    world.mainloop()

