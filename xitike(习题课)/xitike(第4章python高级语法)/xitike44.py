#
# """
# 编写一个程序, 统计当前目录下每个文件类型的文件数
#
# 思路:
#     1. 打开当前文件夹
#     2. 获取当前文件夹下面所有的文件
#     3. 处理我们当前文件夹下面可能有文件的情况
#     4. 做成统计
# """
# import os
#
# # 获取当前文件夹下面所有文件夹
# all_files = os.listdir(os.curdir)  # os.curdir表示当前目录 curdir: currentdirectory
#
# type_dict = dict()
#
# for each_file in all_files:
#     # 如果说我们的each_file是文件夹
#     if os.path.isdir(each_file):
#         type_dict.setdefault("文件夹", 0)
#         type_dict["文件夹"] += 1
#     else:
#         # 如果不是文件夹, 而是文件,统计我们的文件
#         ext = os.path.splitext(each_file)[1]  # 获得文件的后缀
#         type_dict.setdefault(ext, 0)
#         type_dict[ext] += 1
# print(type_dict)
# for each_type in type_dict:
#
#     print("该文件下类型{}的文件{}个".format(each_type, type_dict[each_type]))



"""
编写一个程序,计算当前文件夹下面所有文件的大小
1. 打开当前文件夹
2. 获取到所有文件, 和文件大小
3. 保存我们获取到的数据,然后打印出来
"""

import os

all_files = os.listdir(os.curdir)
file_dict = dict()

for each_file in all_files:
    # 判断我们的这个each_file是不是文件
    if os.path.isfile(each_file):
        file_siza = os.path.getsize(each_file)
        file_dict[each_file] = file_siza

for each in file_dict.items():
    print("{} 大小 {}".format(each[0], each[1]))


"""
编写一个程序,计算当前文件夹下面所有文件的大小
1. 打开当前文件夹
2. 获取到所有文件, 和文件大小
3. 保存我们获取到的数据,然后打印出来
这个是其他盘的,就有写路径了
"""

import os

all_file2 = os.listdir(r"D:\迅雷下载\\")
file_dict = dict()

for each_file in all_file2:
    # 判断我们的这个each_file是不是文件
    if os.path.isfile(r"D:\迅雷下载\\" + each_file):
        file_siza = os.path.getsize(r"D:\迅雷下载\\" + each_file)
        file_dict[each_file] = file_siza

for each in file_dict.items():
    print("{} 大小 {}".format(each[0], each[1]))
