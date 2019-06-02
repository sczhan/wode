
import tkinter

import actor
import config


class Bee(actor.Actor):
    """
     移动的敌军 - 小蜜蜂
    """
    def __init__(self, root, canvas, position, x, y, tags):
        super().__init__(root, canvas, position, x, y, tags, config.image_bee_width,
                                  config.image_bee_height, True)

        # 移动者的移动步长
        self.steps = [config.step_length_bee_x, config.step_length_bee_y]
        # 移动方向 - 向下
        self.move_direction = [1, 1]
        # 移动者加载背景图像
        self.bg_image_fullname = config.image_path + config.filename_bee + config.filename_suffix
        self.bg_image = tkinter.PhotoImage(file=self.bg_image_fullname)
        self.bg_image_tags = tags

    def exec_move(self):
        """
        碰壁
        :return: none
        """
        # 左右碰壁是x轴反向
        if self.nw[0] < self.steps[0] or \
                self.ne[0] > config.window_boundary_col - self.steps[0]:
            self.move_direction[0] *= -1
        # y 轴 边界之内正常移动
        if self.nw[1] < config.window_boundary_row:
            x = self.steps[0] * self.move_direction[0]
            y = self.steps[1] * self.move_direction[1]
            self.base_move(self.bg_image_tags, x, y)
        # 边界之外错误处理
        else:
            self.base_move(self.bg_image_tags, 0, -config.window_boundary_row)

    # 获取死亡图片
    def get_dead_image(self):
        """
        :return: none
        """
        img = []
        if self.do_dead_play:
            for i in self.dead_image_index:
                image_fullname = config.images_path + config.filename_bee \
                    + str(i) + config.filename_suffix
                image = tkinter.PhotoImage(file=self.bg_image_fullname)
                img.append(image)
            return img




