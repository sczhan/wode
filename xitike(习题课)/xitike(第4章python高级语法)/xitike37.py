
# 编写一个计算减法的方法, 当第一个数小于第二个数时, 抛出"被减数不能小于减数的异常"


# def jianfa(a, b):
#     if int(a) < int(b):
#         raise BaseException("被减数不能小于减数")
#     else:
#         return int(a) - int(b)
#
# try:
#     jianfa(3, 7)
# except BaseException as error:
#     print("好像出错了, 出错的内容是{}".format(error))


# 定义一个函数func(filename)filename: 文件路径,
# 函数功能: 打开文件, 并且返回文件内容, 最后关闭, 用异常来处理可能发生的错误
#
# import os
#
#
# def func(filename):
#     try:
#         file = open(filename)
#     except Exception as error:
#         print("出错了, 出错的内容是{}".format(error))
#     else:
#         print(file.read())
#         file.close()
#
#
# func("haha.txt")



# 自己定义一个异常类, 继承Exceptionlei, 铺货下面过程:判断输入的字符串长度是是否小于5
#
#
# class MyError(Exception):
#     def __init__(self, str):
#         self.str = str
#
#     def process(self):
#         if len(self.str) < 5:
#             print("字符串长度必须大于5")
#         else:
#             print("算你聪明")
#
# try:
#     er = MyError("ssss")
#     er.process()
# except MyError as error:
#     print(error)



def jianfa(a, b):
    try:
        if int(a) < int(b):
            raise BaseException("被减数不能小于减数")
        else:
            return a - b
    except BaseException as error:
        print("好像出错了, 出错的内容是{}".format(error))


print(jianfa(8, 7))