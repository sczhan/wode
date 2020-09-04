#
# def fb(i):
#     if i == 1 or i == 2:
#         return 1
#     return fb(i-1) + fb(i-2)
#
# print(fb(7))
#
# i = 1
# a = 1
# b = 1
# while i<8:
#     if i == 1 or i == 2:
#         print(1)
#     else:
#         a, b = a + b, i-2
#         print(a)
#     i += 1
def addUser(contactlist):
    # 1.增加姓名和手机
    name = input("请输入姓名:>")
    # 判断姓名，在列表当中是否已经存储，如果存储，就提示用户不能存储，否则就存入
    flag = False  # 默认此人没存储过
    for index in range(len(contactlist)):
        if (contactlist[index][0] == name):
            print("此联系人已经存在，请重新输入！！")
            flag = True  # 设置此人已经存储
            break

    if not flag:
        phone = input("请输入手机号:>")
        singlelist = [name, phone]
        # 将一个人信息组成的列表，添加到总体的列表当中
        contactlist.append(singlelist)
        print("输入完成")


def deleteUser(contactlist):
    # 2.删除姓名
    name = input("请输入要删除的联系人:>")
    flag = False  # 默认这个人不存在
    # 遍历列表，查看这个列表当中是否包含此人
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            # 说明此人存在
            del contactlist[index]
            flag = True
            print("删除成功")
            break
    if not flag:
        print("查无此人！")


def updateUser(contactlist):
    # 3.修改手机号码
    name = input("请输入要修改的联系人:>")
    flag = False  # 默认这个人不存在
    # 遍历列表，查看这个列表当中是否包含此人
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            # 说明此人存在
            phone = input("请输入要修改的电话号码:>")
            contactlist[index][1] = phone
            flag = True
            print("修改成功")
            break

    if not flag:
        print("查无此人！")


def getAllUser(contactlist):
    # 4.查询所有用户
    print("-------------------")
    for i in contactlist:
        print("用户：\t%s\t\t%s" % (i[0], i[1]))
    print("-------------------")


def queryPhoneByName(contactlist):
    # 5.根据姓名查找手机号
    name = input("请输入要查询的联系人:>")
    flag = False  # 默认这个人不存在
    # 遍历列表，查看这个列表当中是否包含此人
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            # 说明此人存在
            print("您要查找的手机号码是：%s" % (contactlist[index][1]))
            flag = True
            break
    if not flag:
        print("查无此人！")


def work(contactlist):
    while True:
        num = input("请根据规则继续输入:>")
        # 判断用户输入码是否在1，2，3，4，5，6当中
        if num not in ['1', '2', '3', '4', '5', '6']:
            print("输入有误，请重新输入")
        else:
            if num == '1':
                addUser(contactlist)
            elif num == '2':
                deleteUser(contactlist)
            elif num == '3':
                updateUser(contactlist)
            elif num == '4':
                getAllUser(contactlist)
            elif num == '5':
                queryPhoneByName(contactlist)
            elif num == '6':
                # 6.退出
                print("感谢使用")
                break


def main():
    # 因为可能存储多组数据，创建一个列表，目前列表没有元素，所以为空列表
    contactlist = []
    info = '''
    ====通讯录管理系统====
    1.增加姓名和手机
    2.删除姓名
    3.修改手机
    4.查询所有用户
    5.根据姓名查找手机号
    6.退出
    =====================
    '''
    print(info)
    work(contactlist)


if __name__ == "__main__":
    main()