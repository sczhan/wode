
import tkinter

"""
蜜蜂从上向下运动
可以通过键盘左右控制
"""
step = 0  # 计算器,计算一个走了多少步
direction = (1, 1)

x = 0
y = 10


def set_right(e):
    """

    :param e:
    :return:
    """
    global x
    x += 20


def set_left(e):
    """

    :param e:
    :return:
    """
    global x
    x -= 20


root_window = tkinter.Tk()
root_window.title("world")

root_window.bind("<Key-Left>", set_left)
root_window.bind("<Key-Right>", set_right)
# 设置不能更改宽,高
root_window.resizable(width=False, height=False)
window_canvas = tkinter.Canvas(root_window, width=450, height=600)
window_canvas.pack()


def main():
    # 创建开始界面
    bg_img_name = "../img/background.gif"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    # tags 的作用是,以后我们使用创建好的image可以通过tags使用
    window_canvas.create_image(480/2, 600/2, anchor=tkinter.CENTER, image=bg_img, tags="bg")

    # 画上一个小蜜蜂
    bee = "../img/bee.gif"
    bee_img = tkinter.PhotoImage(file=bee)
    window_canvas.create_image(150, 180/2, anchor=tkinter.CENTER, image=bee_img, tags="bee")

    sp = "../img/smallplane.gif"
    sp_img = tkinter.PhotoImage(file=sp)
    window_canvas.create_image(50, 100/2, anchor=tkinter.CENTER, image=sp_img, tags="sp")
    # 让小飞机动起来
    ap_move()
    tkinter.mainloop()


def ap_move():
    """
    :return:
    """
    global step
    global x
    global y
    y += 20
    print(x, y)
    window_canvas.move("sp", x, y)
    window_canvas.move("bee", x, y)
    step += 1
    window_canvas.after(1000, ap_move)


if __name__ == "__main__":
    main()

