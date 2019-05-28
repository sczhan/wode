
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
num3 = ""
num4 = ""
num7 = ""
num8 = ""
num10 = ""
num12 = ""
operatio = ""


def delete():
    """
    :return:
    """
    global num1
    global num2
    global operatio
    if not operatio:
        num1 = num1[:-1]
        sv.set(num1)
    else:
        num2 = num2[:-1]
        sv.set(num1 + operatio + num2)
    if not num1:
        sv.set("0")


def change(num):
    """
    :param num:数字
    :return:
    """
    global num1
    global num2
    global num3
    global num10
    global num12
    if operatio not in ["+", "-", "x", "/"]:
        num1 = num1 + num
        sv.set(num1)

    else:
        num2 = num + num2
        # sv.set(num1 + operatio + num2)

        if operatio:
            num10 = num10 + num
            sv.set(num1 + operatio + num2 + operatio + num10)


def operation(op):
    """
    :param op:操作符
    :return:
    """
    global num1
    global num2
    global operatio
    if op in ["+", "-", "x", "/"]:
        operatio = op

    else:
        if operatio == "+":
            if num7 != "" or num8 != "":
                rst1 = float(num1) + float(num2)
                if len(num1) >= len(num2):
                    rst1 = str(rst1)
                    rst = rst1[:len(num1)]
                    sv.set(rst)
                    print(rst)
                else:
                    rst1 = str(rst1)
                    rst = rst1[:len(num2)]
                    sv.set(rst)
                    print(rst)
            else:
                rst = int(num1) + int(num2) + int(num10)
                sv.set(rst)

        if operatio == "-":
            if num7 != "" or num8 != "":
                rst1 = float(num1) - float(num2)
                if len(num1) >= len(num2):
                    rst1 = str(rst1)
                    rst = rst1[:len(num1)]
                    sv.set(rst)
                    print(rst)
                else:
                    rst1 = str(rst1)
                    rst = rst1[:len(num2)]
                    sv.set(rst)
                    print(rst)
            else:
                rst = int(num1) - int(num2)
                sv.set(rst)

        if operatio == "x":
            if num7 != "" or num8 != "":
                rst1 = float(num1) * float(num2)
                rst1 = str(rst1)
                rst = rst1[:len(num1)+len(num2)]
                sv.set(rst)
                print(rst)
            else:
                rst = int(num1) * int(num2)
                sv.set(rst)

        if operatio == "/":
            if num7 != "" or num8 != "":
                rst1 = float(num1) / float(num2)
                rst = rst1
                sv.set(rst)
            else:
                if int(num1) % int(num2) == 0:
                    rst1 = int(num1) / int(num2)
                    rst1 = str(rst1)
                    rst = rst1[:-2]
                    sv.set(rst)
                else:
                    rst = int(num1) / int(num2)
                    rst = str(rst)
                    sv.set(rst[:11])


def clear():
    global num1
    global num2
    global num7
    global num8
    global operatio
    num1 = ""
    num2 = ""
    num7 = ""
    num8 = ""
    operatio = ""
    sv.set("0")


def fan():
    global num1
    global num2
    global operatio
    if not operatio:
        num1 = - int(num1)
        num1 = str(num1)
        sv.set(num1)
    else:
        num2 = -int(num2)
        num2 = str(num2)
        sv.set(num1 + operatio + num2)


def pfang():
    global num1
    global num2
    global operatio
    if not operatio:
        num1 = int(num1) * int(num1)
        num1 = str(num1)
        sv.set(num1)
    else:
        if operatio in ["+", "-", "x", "/"]:
            sv.set(num1)
        else:
            num2 = int(num2) * int(num2)
            num2 = str(num2)
            sv.set(num1 + operatio + num2)



def dian():
    global num1
    global num2
    global num3
    global num4
    global num7
    global num8
    global operatio

    if num1:
        if dian:
            num5 = num1 + "." + num3
            num1 = num5
            num7 = 2
    if num2:
        if dian:
            num6 = num2 + "." + num4
            num1 = num5[:-1]
            num2 = num6
            num8 = 2


# 第二布: 画出图像界面下面部分
frame_bord = Frame(width=400, height=350, bg="#cccccc")
b_del = Button(frame_bord, text="←", width=6, height=2, command=delete).grid(row=0, column=0)
b_1 = Button(frame_bord, text="1", width=6, height=2, command=lambda: change("1")).grid(row=1, column=0)
b_2 = Button(frame_bord, text="2", width=6, height=2, command=lambda: change("2")).grid(row=1, column=1)
b_3 = Button(frame_bord, text="3", width=6, height=2, command=lambda: change("3")).grid(row=1, column=2)
b_4 = Button(frame_bord, text="4", width=6, height=2, command=lambda: change("4")).grid(row=2, column=0)
b_5 = Button(frame_bord, text="5", width=6, height=2, command=lambda: change("5")).grid(row=2, column=1)
b_6 = Button(frame_bord, text="6", width=6, height=2, command=lambda: change("6")).grid(row=2, column=2)
b_7 = Button(frame_bord, text="7", width=6, height=2, command=lambda: change("7")).grid(row=3, column=0)
b_8 = Button(frame_bord, text="8", width=6, height=2, command=lambda: change("8")).grid(row=3, column=1)
b_9 = Button(frame_bord, text="9", width=6, height=2, command=lambda: change("9")).grid(row=3, column=2)
b_0 = Button(frame_bord, text="0", width=6, height=2, command=lambda: change("0")).grid(row=4, column=1)
b_jia = Button(frame_bord, text="+", width=6, height=2, command=lambda: operation("+")).grid(row=1, column=3)
b_jian = Button(frame_bord, text="-", width=6, height=2, command=lambda: operation("-")).grid(row=2, column=3)
b_cheng = Button(frame_bord, text="x", width=6, height=2, command=lambda: operation("x")).grid(row=3, column=3)
b_chu = Button(frame_bord, text="/", width=6, height=2, command=lambda: operation("/")).grid(row=4, column=3)
b_dyu = Button(frame_bord, text="=", width=6, height=2, command=lambda: operation("=")).grid(row=4, column=2)
b_dian = Button(frame_bord, text=".", width=6, height=2, command=dian).grid(row=4, column=0)
b_C = Button(frame_bord, text="C", width=6, height=2, command=clear).grid(row=0, column=1)
b_jj = Button(frame_bord, text="±", width=6, height=2, command=fan).grid(row=0, column=2)
b_pf = Button(frame_bord, text="x²", width=6, height=2, command=pfang).grid(row=0, column=3)

# 也可以这么写
# b_1 = Button(frame_bord, text="1", width=6, height=2, command=lambda: change("1"))
# b_2 = Button(frame_bord, text="2", width=6, height=2, command=lambda: change("2"))
# b_3 = Button(frame_bord, text="3", width=6, height=2, command=lambda: change("3"))
# b_jia = Button(frame_bord, text="+", width=6, height=2, command=lambda: operation("+"))
# b_dyu = Button(frame_bord, text="=", width=6, height=2, command=lambda: operation("="))
# b_1.grid(row=1, column=0)
# b_2.grid(row=1, column=1)
# b_3.grid(row=1, column=2)
# b_jia.grid(row=1, column=3)
# b_dyu.grid(row=4, column=2)
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


# 问题:三个数及以上的加减
