"""
编写一个程序,当用户输入一个文件名和行数的时候, 将该文件的前N行打印到屏幕上
input 接受一个文件名
input 接受行数
"""
# filename = input("文件名:")
# line_num = input("请输入你要显示的前几行")
#
#
# def file_view(file_name, line_num):
#     print("\n文件%s的前%s行的内容如下" % ( file_name, line_num))
#     f = open(filename)
#     for i in range(int(line_num)):
#         print(f.readline())
#
#     f.close()
#
# file_view(filename, line_num)


# filename = input("文件名:")
# line_num = input("请输入你要显示的前几行")
# z = []
# d = lambda x, y: [z.append(linecache.getline(x, int(i)).split()) for i in range(1, int(y)+1)]
# d(filename, line_num)
# for zl in z:
#     for zzl in zl:
#         print(zzl)

"""
在上面基础上, 用户可以随意输入显示的行数
"""
# filename = input("文件名:")
# start_lnum = input("请输入开始行:")
# end_lnum = input("请输入结束行:")
#
#
# def file_view(a, b, c):
#     f = open(str(a))
#     if b == "1":
#         print(f.readline())
#     if b == ":" and c == ":":
#         print(f.read())
#     if b > "1" and b != ":":
#         for i in range(int(b)-1):
#             f.readline()
#     if c != ":":
#         for i in range(int(c)-1):
#             print(f.readline())
#     else:
#         print(f.read())
#     f.close()
#
#
# file_view(filename, start_lnum, end_lnum)

#
# filename = input("文件名:")
# lnum = input("请输入显示行数, 1:2")
#
#
# def print_lnum(a, b):
#     f = open(a)
#
#     start, end = lnum.split(":")
#
#     if start == "":
#         start = "1"
#
#     if end == "":
#          end = "-1"
#
#     start = int(start) - 1
#     end = int(end)
#     lines = end - start
#
#     for i in range(start):
#         f.readline()
#
#     if lines <= 0:
#         print(f.read())
#     else:
#         for j in range(lines):
#             print(f.readline())
#     f.close()
#
#
# print_lnum(filename, lnum)


"""
编写一个程序, 实现"全部替换"的功能
- 打开一个文件
- 把文件中 xxx  替换成 sss
- open 打开文件
- readline 读取文件内容
- replace 替换
"""
filename = input("请输入文件名:")
rep_work = input("请输入要替换的字符:")
new_word = input("请输入新替换的字符串")


def file_repalce(f_n, rep_word, new_word):
    f = open(f_n)
    contenct = []
    for each in f:
        if rep_word in each:
            each = each.replace(rep_word, new_word)
        contenct.append(each)
    decide = input("确定要折磨做吗? 请输入yes/no")

    if decide in ["YES", "Yes", "yes"]:
        f_write = open(f_n, "w")
        f_write.write("".join(contenct))
        f_write.close()


file_repalce(filename, rep_work, new_word)


