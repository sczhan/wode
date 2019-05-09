
# 打印字母A
# 控制行
#
# def a():
#     for i in range(5):
#         # 判断开始输入的位置
#         for j in range(4-i):
#             print(" ", end="")
#         # 控制行
#         for j in range(i+1):
#             if i ==0 or i == 2:
#                 print("* ", end="")
#                 continue
#             if j == i or j == 0:
#                 print("* ", end="")
#                 continue
#             else:
#                 print("  ", end="")
#         print()
#
#
# a()

# 打印B
for i in range(5):
    for j in range(4):
        if i == 2 or i == 0 or i == 4:
            if j < 3:
                print("*", end=" ")
                continue
        if j == 3 or j == 0:
            if i == 1 or i == 3:
                print("*", end=" ")
                continue
        else:
            print(" ", end=" ")
    print()