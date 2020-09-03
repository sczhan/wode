
import random
name, password, card = [], [], []
name_log = ""
new_card = 1000


def registered():
    global name, password, card, new_card
    new_name = input("注册名: ")
    new_password = input("密码: ")
    if new_name in name:
        print("该用户名已存在")
    if new_name == "" or new_password == "":
        print("注册名或者密码不能为空")
    new_card += 1
    name.append(new_name)
    password.append(new_password)
    card.append(new_card)
    print("会员名  {}  密码  {}  会员卡号  {}".format(new_name, new_password, new_card))


def login():
    global name, password, card, name_log
    print("*****登录****")
    login_name = input("请输入会员名: ")
    login_password = input("请输入密码: ")
    if login_name not in name:
        print("会员名不存在: ")
    elif (login_name in name) and (login_password in password) and \
            (login_password == password[name.index(login_name)]):
        print("登录成功, 欢迎您{}".format(login_name))
        name_log = login_name
    else:
        print("会员名. 密码不正确")
    return name_log


def lucky_draw():
    global name, card, name_log
    number = random.randint(0, 9)
    if name_log == "":
        print("请登录在抽奖")
    else:
        print("*****抽奖****")
        login_card = card[name.index(name_log)]
        print("{} 您的卡号为: {}".format(name_log, login_card))
        if number == login_card % 1000:
            print("恭喜你, 中奖了. 本次中奖的个位数为: {}".format(number))
        else:
            print("很遗憾, 您没中奖. 本次中奖的个位数为: {}".format(number))



def menu():
    while True:
        print("------奖客富翁系统------")
        s = input("请选择你的操作: 1注册 2登录 3抽奖 0退出: ")
        if s == "1":
            print("进入注册功能模块")
            registered()
        elif s == "2":
            print("进入登录功能模块")
            login()
        elif s == "3":
            print("进入抽奖功能模块")
            lucky_draw()
        elif s == "0":
            print("欢迎下次光临")
            break
        else:
            print("请选择正确菜单")


if __name__ == '__main__':
    menu()
