
import tkinter


if __name__ == "__main__":
    root_windows = tkinter.Tk()
    root_windows.title("飞机大战")
    root_windows.resizable(width=False, height=False)
    # 创建画布
    windows_canvas = tkinter.Canvas(root_windows, width=480, height=600)
    windows_canvas.pack()
    # 在画布上画一个图片
    # 三个步骤
    # 1.定义图片位置
    # 2.创建PhotoImage对象
    # 3. 利用create_image函数把图片画上去
    bg_img_name = "../img/background.gif"
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    # tags 的作用是,以后我们使用创建好的image可以通过tags使用
    windows_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bg_img, tags="bg")

    # 画上一个小蜜蜂
    bee_img_name = "../img/bee.gif"
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    windows_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bee_img, tags="bee")

    root_windows.mainloop()
