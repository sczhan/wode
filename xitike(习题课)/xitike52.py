#
# # 用tkinter写一个小游戏, 来随机生成我们需要的名字
#
# import tkinter
# import random
#
# window = tkinter.Tk()
#
#
# def random_1():
#     s1 = ["cats", "hippos", "cakes"]
#     s = random.choice(s1)
#     return s
#
#
# def random_2():
#     s2 = ["eats", "likes", "hates", "has"]
#     s = random.choice(s2)
#     return s
#
#
# def button_click():
#     name = nameEntry.get()
#     verb = random_1()
#     noum = random_2()
#     sentence = str(name) + "" + str(verb) + "" + str(noum)
#     result.delete(0, tkinter.END)
#     result.insert(0, sentence)
#
#
# nameLabel = tkinter.Label(window, text="Name:")
# nameEntry = tkinter.Entry(window)
# button = tkinter.Button(window, text="生成随机名称", command=button_click)
# result = tkinter.Entry(window)
#
# nameLabel.pack()
# nameEntry.pack()
# button.pack()
# result.pack()
#
# window.mainloop()


# # 输入密码的小程序, 我们自己设定一个密码, 如果用户输入正确则显示正确, 否则显示不正确
#
# import tkinter as tk
#
# window = tk.Tk()
#
# def check_password():
#     password = "123456"
#     entered_password = passwordEntry.get()
#     if password == entered_password:
#         confirmLabel.config(text="正确")
#     else:
#         confirmLabel.config(text="不正确")
#
#
# passwordLabel = tk.Label(window, text="Password")
# passwordEntry = tk.Entry(window, show="*")
# button = tk.Button(window, text="校验", command=check_password)
# confirmLabel = tk.Label(window)
# passwordLabel.pack()
# passwordEntry.pack()
# button.pack()
# confirmLabel.pack()
# window.title("密码")
# window.mainloop()


# 一个猜数字的小游戏, 计算机随机生成一个整数, 用户数日去猜这个整数,
# 如果用户输入正确,那么分数加1, 并且显示计算机生成数字
# 如果用户输入不正确, 那么我们的分数不变, 还是要显示生成的数字

import random
import tkinter as tk

window = tk.Tk()

maxNo = 10
score = 0
rounds = 0


def button_clik():
    global score
    global rounds

    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNo:
            result = random.randrange(1, maxNo+1)
            if guess == result:
                result = "正确答案: " + str(result)
                score += 1
            else:
                result = "正确答案: " + str(result)
            rounds += 1
        else:
            result = "输入不合法"
    except:
        result = "输入不合法"
    resultLabel.config(text=result)
    scoreLabel.config(text="score: " + str(score) + "\nrounds: " + str(rounds))
    guessBox.delete(0, tk.END)


resultLabel = tk.Label(window)
scoreLabel = tk.Label(window)
guessBox = tk.Entry(window)
guessLabel = tk.Label(window, text="请输入1到" + str(maxNo))
button = tk.Button(window, text="guess", command=button_clik)

scoreLabel.pack()
resultLabel.pack()
guessBox.pack()
guessLabel.pack()
button.pack()

window.mainloop()

help(tk.Label.config)