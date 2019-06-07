
# 包含一个学生类,
# 一个sayhello函数,
# 一个打印语句


class Student(object):
    """
    学生类
    """
    def __init__(self, name="Noname", age=18):
        self.name = name
        self.age = age

    def say(self):
        """
        打招呼
        :return:self.name self.age
        """
        print("My name is {0}".format(self.name))


def sayhello():
    """
    :return: none
    """
    print("Hi, 欢迎来到这里")


# 此判断语句建议一直作为程序的入口
if __name__ == "__main__":
    print("我是模块p01")