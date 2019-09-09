
"""
编写一个程序, 接受用户输入的内容, 并且保存新的文件
如果用过单独输入 ":w", 表示文件保存退出
open()
input()
"w"
"""
# file_name = input("请输入文件名: ")
#
#
# def file_write(file_name):
#     f = open(file_name, "w")
#     print("请输入内容(:w 保存退出)")
#
#     while True:
#         write_something = input()
#         # 判断输入是不是:w
#         if write_something != ":w":
#             f.write("%s\n" % write_something)
#         else:
#             break
#
#     f.close()


# file_write(file_name)




"""
编写一个程序, 比较用户输入的文件是否相同, 如果结果不同,显示出所有不同处的行号
f.readline()
open()
differ
"""

file1 = input("请输入第一个文件名")
file2 = input("请输入第二个文件名")


def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)

    count = 0
    differ = []

    for line1 in f1:
        print(line1)
        line2 = f2.readline()
        print(line2)

        count += 1

        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()

    return differ


differ = file_compare(file1, file2)

if len(differ) == 0:
    print("两个文件相同")
else:
    print("两个文件有%d不同" %len(differ))
    for each in differ:
        print("第%d行不一样" %each)


a = ["a", "b", "c"]
c = lambda  a: ([a[i] + str(i) for i in range(3)])
print(c(a))