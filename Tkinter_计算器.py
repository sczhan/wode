
# Tkinter - 计算器
#  模拟系统的计算器功能
#  实现一个简单的具有加减法等操作的计算器
#  操作步骤
#   1.画GUI
#   2.给每个控件配置相应的事件
#   3.写逻辑代码
# 第一步: 画出图形界面上部
from tkinter import *
root = Tk()
root.title("计算器")
# 定义面板的大小
root.geometry("250x380")
# bg代表背景颜色(background), #dddddd 是十六进制表示颜色的一个串
frame_show = Frame(width=300, height=150, bg="#dddddd")
frame_show.pack()
# 定义顶部区域
sv = StringVar()
sv.set("0")

# anchor:定义控件的锚点,e代表右边(东) w代表右边(西),n代表上(北),s代表下(南)
show_label = Label(frame_show, textvariable=sv, bg="green", width=12, height=1,
                   font=("黑体", 20, "bold"), justify=LEFT,
                   anchor="e")

show_label.pack(padx=10, pady=10)
# root.mainloop()

num1 = ""
num2 = ""
operatio = ""


def delete():
    """

    :return:
    """
    pass


def change(num):
    """

    :param num:数字
    :return:
    """
    global num1
    global num2
    if not operatio:
        num1 = num1 + num
        sv.set(num1)

    else:
        num2 = num2 + num
        sv.set(num1 + operatio + num2)


def operation(op):
    """
    :param op:操作符
    :return:
    """
    global operatio
    if op in ["+", "-", "x", "/"]:
        operatio = op

    else:
        if operatio == "+":
            rst = int(num1)+int(num2)
        if operatio == "-":
            rst = int(num1) - int(num2)
        if operatio == "x":
            rst = int(num1) * int(num2)
        if operatio == "/":
            rst = int(num1) / int(num2)
        sv.set(rst)


# 第二布: 画出图像界面下面部分
frame_bord = Frame(width=400, height=350, bg="#cccccc")
b_del = Button(frame_bord, text="←", width=6, height=1, command=delete)
b_del.grid(row=0, column=0)
b_1 = Button(frame_bord, text="1", width=6, height=2, command=lambda: change("1"))
b_2 = Button(frame_bord, text="2", width=6, height=2, command=lambda:  change("2"))
b_3 = Button(frame_bord, text="3", width=6, height=2, command=lambda:  change("3"))
b_jia = Button(frame_bord, text="+", width=6, height=2, command=lambda: operation("+"))
b_dyu = Button(frame_bord, text="=", width=6, height=2, command=lambda: operation("="))

b_1.grid(row=1, column=0)
b_2.grid(row=1, column=1)
b_3.grid(row=1, column=2)
b_jia.grid(row=1, column=3)
b_dyu.grid(row=2, column=3)
frame_bord.pack(padx=10, pady=10)

# 第三步: 添加逻辑功能
# 考虑以下几种情况
#  1.按下数字
#  2.按下操作符
#  3.只考虑两个操作数操作,比考虑复杂情况
"""
num1 = ""
num2 = ""
operator = ""
    def change(num):
        # 按下一个数字需要考虑两种情况
        #  1. 数字属于第一个操作数
        #  2. 数字属于第二个操作数
        #  3. 判断是否属于第一个操作数,可以通过operator判断
        if not operator:
            num1 = num1 + num
            # 如果是第一个操作数,则只显示第一个操作数
            sv.set(num1)
        else:
            num2 = num2 + num
            # 如果是第二个操作符,则应该显示完整的计算式子
            sv.set(num1 + operator + num2)
        
    def operation(op):
        if op in ["+", "-", "*", "/"]:
            operator = op
        else:  #认为按下的等于号
            if op == "+":
                rst = int(num1) + int(num2)
                ...
            
"""

root.mainloop()