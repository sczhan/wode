
class Game_zimu(object):
    # 打印字母A
    # 控制行

    def a(self):
        for i in range(5):
            # 判断开始输入的位置
            for j in range(4-i):
                print(" ", end="")
            # 控制行
            for j in range(i+1):
                if i ==0 or i == 2:
                    print("* ", end="")
                    continue
                if j == i or j == 0:
                    print("* ", end="")
                    continue
                else:
                    print("  ", end="")
            print()

    # a()

    # 打印B

    def b(self):
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

    # b()

    # 打印C
    def c(self):
        for i in range(4):
            for j in range(4):
                if i == 0 or i == 3:
                    if j == 0:
                        print("  ", end="")
                    else:
                        print("* ", end="")
                elif i == 2 or i == 1:
                    if j == 0:
                        print("* ",end="")
                else:
                    print(" ", end="")
            print()

    # c()

    # 打印d
    def d(self):
        for i in range(4):
            for j in range(5):
                if i == 0 or i == 3:
                    if j < 3:
                        print("* ", end="")
                    continue
                if j == 0:
                    print("*  ", end="")
                if i == 1 or i == 2:
                    if j == 4:
                        print("*  ", end="")
                    else:
                        print(" ", end="")
            print()

    # d()

    # 打印E
    def e(self):
        for i in range(5):
            for j in range(5):
                if i == 0 or i == 2 or i == 4:
                    print("* ", end="")
                    continue
                if j == 1:
                    print("* ",end="")
            print()

    # e()

    # 打印F
    def f(self):
        for i in range(5):
            for j in range(5):
                if i == 0 or i == 2:
                    print("* ", end="")
                    continue
                if j == 1:
                    print("* ",end="")
            print()

    # f()

    # 打印G
    def g(self):
        for i in range(4):
            for j in range(5):
                if i == 0 or i == 3:
                    if j > 0:
                        print("* ", end="")
                    else:
                        print("  ", end="")
                elif j == 0:
                    print("* ", end="")
                elif i == 2:
                    if j == 4 or j == 3:
                        print("* ", end="")
                    else:
                        print("  ", end="")
            print()

    # g()

    # 打印H
    def h(self):
        for i in range(5):
            for j in range(4):
                if j == 0 or j == 3:
                    print("* ", end="")
                    continue
                if i == 2:
                    if j == 1 or j == 2:
                        print("* ", end="")
                else:
                    print("  ", end="")
            print()

    # h()

    # 打印I
    def i(self):
        for i in range(5):
            for j in range(5):
                if i == 0 or i == 4:
                    print("* ", end="")
                    continue
                if i == 1 or i == 2 or i == 3:
                    if j == 2:
                        print("* ", end="")
                    else:
                        print("  ", end="")
            print()

    # i()

    # 打印J
    def j(self):
        for i in range(5):
            for j in range(5):
                if i == 0:
                    print("* ", end="")
                    continue
                if i == 1 or i == 2 or i == 3:
                    if j == 2:
                        print("* ", end="")
                        continue
                if i == 4 and j == 1 or i == 3 and j == 0:
                    print("* ", end="")
                    continue
                else:
                    print("  ", end="")
            print()

    # j()

    # 打印K
    def k(self):
        for i in range(5):
            for j in range(4):
                if j == 0:
                    print("* ", end="")
                    continue
                if j == 3-i and i < 3:
                    print("* ", end="")
                    continue
                if j == i-1 and i >= 3:
                    print("* ", end="")
                    continue
                else:
                    print("  ", end="")
            print()

    # k()

    # 打印L
    def l(self):
        for i in range(5):
            for j in range(5):
                if i == 4:
                    print("* ", end="")
                    continue
                if j == 1:
                    print("* ", end="")
            print()

    # l()

    # 打印M
    def m(self):
        for i in range(5):
            for j in range(4-i):
                    print(" ", end="")
                # 控制行
            for j in range(i+1):
                if i == 0:
                    print("* ", end="")
                    continue
                if j == i or j == 0:
                    print("* ", end="")
                    continue
                else:
                    print("  ", end="")
            for j in range(4-i):
                    print("  ", end="")
                    # 控制行
            for j in range(i+1):
                if i == 0:
                    print("* ", end="")
                    continue
                if j == i or j == 0:
                    print("* ", end="")
                    continue
                else:
                    print("  ", end="")
            print()

    # m()

    # 打印N
    def n(self):
        for i in range(5):
            for j in range(5):
                if j == 0 or j == 4:
                    print("* ", end="")
                else:
                    print("  ", end="")
                if i == 1 or i == 2 or i == 3:
                    if i == j+1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
            print()

    # n()


# zimu = Game_zimu()
# zimu.j()
