#
# visits = [200, 388, 123, 456, 987, 342, 767, 234, 124, 345, 123, 234]
#
#
# def visit(start, end):
#     new_visit = visits[int(start) - 1: int(end)]
#     ping = int(sum(new_visit) / len(new_visit))
#     print("{}月~{}月平均访客量:  {}".format(start, end, ping))
#
#
# if __name__ == '__main__':
#     while True:
#         a = input("请输入开始月份: ")
#         b = input("请输入结束月份: ")
#         if a.isdigit() and b.isdigit():
#             visit(a, b)
#             break
#         else:
#             print("输入有误")

# def holiday(year):
#     year = int(year)
#     if year < 5:
#         print("工龄是{}年的员工的年假是 :  1".format(year))
#     elif year < 10:
#         print("工龄是{}年的员工的年假是 :  5".format(year))
#     else:
#         print("工龄是{}年的员工的年假是 :  7".format(year))
#
#
# if __name__ == '__main__':
#     while True:
#         a = input("请输入工龄: ")
#         if a.isdigit():
#             holiday(a)
#             break
#         else:
#             print("输入有误")
import random

red_lists = []
red_list = [i for i in range(1, 34)]
for i in range(6):
    red = random.choice(red_list)
    red_lists.append(red)
    if red in red_list:
        red_list.pop(red_list.index(red))
    else:
        red_lists.append(red)

blue = random.randint(1, 17)
red_lists.sort()

if __name__ == '__main__':
    print("红球: ", red_lists)
    print("蓝球: ", blue)
    while True:
        a = input("继续生成吗(Y/N) ? ")
        if a == "N":
            print("谢谢使用")
            break
        else:
            print("红球: ", red_lists)
            print("蓝球: ", blue)