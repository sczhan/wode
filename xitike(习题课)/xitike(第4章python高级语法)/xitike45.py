#
# """
# 编写一个程序, 用户输入文件名以及开始搜索的路径, 搜索该文件是否存在, 如果遇到文件夹,则进入文件夹继续搜索
# input : 接受用户输入文件名和开始搜索的路径
# so.path.isdir : 去判断是不是文件夹,如果是的话, 就需要进入该文件夹继续搜索,循环调用一下我们的函数来实现
# """
# import os
#
# start_dir = input("请输入目录: ")
# target = input("请输入要搜索的文件名: ")
#
#
# def search_file(start_dir, target):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         if each_file == target:
#             print(os.getcwd() + "\\" + each_file)
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)  # 调用父目录
#
#
# search_file(start_dir, target)

#
# """
# 加需求
# 模糊匹配, 判断我们target是否包含在某一个文件中
# - in 去判断target字符串是否在文件的名字中
# """
#
# import os
#
# start_dir = input("请输入目录: ")
# target = input("请输入要搜索的文件名: ")
#
#
# def serach_file(start_dir, target):
#     os.chdir(start_dir)
#
#     for each_file in os.listdir(os.curdir):
#         if target in each_file:
#             print(os.getcwd() + os.sep + each_file)
#         if os.path.isdir(each_file):
#             serach_file(each_file, target)
#             os.chdir(os.pardir)
#
#
# serach_file(start_dir, target)



"""
再加需求, 保存我们的文件存在的地方, 指定的路径
file I/O 写文件
"""
import os

start_dir = input("请输入目录: ")
target = input("请输入要搜索的文件名: ")
backup = []

def serach_file(start_dir, target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        if target in each_file:
            backup_file = os.getcwd() + os.sep + each_file
            backup.append(backup_file)
        if os.path.isdir(each_file):
            serach_file(each_file, target)
            os.chdir(os.pardir)
    return backup


ed = serach_file(start_dir, target)
print(ed)
f = open(os.getcwd() + os.sep + "backup.txt", "wb")
f.write("\n".join(ed).encode("utf-8"))
f.close()