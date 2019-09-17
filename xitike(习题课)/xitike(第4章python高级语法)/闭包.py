
def count():
    def f(j):
        def g():
            print()
            return j*j
        print(str(g) + "##"*20)
        print(g)
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
        # print(str(f(i)) + "**"*20)
    print(fs)

    return fs


f1, f2, f3 = count()
print(f1())
print(f2())

#
# a  = lambda x,y:[i*i for i in range(int(x), int(y))]
# print(a(5, 7))


def count():
    fs = []

    for i in range(1, 4):
        def f():
             print(12)
             return i*i
        # print(str(f) + "***")
        fs.append(f)
        print(123)
    print(f)
    print(fs)
    return fs

f1, f2, f3 = count()
print(f1())
