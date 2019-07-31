

'''
定义一个学生类,用来形容学生
'''
# 定义一个空的类


class Student():
    # 一个空类,pass代表直接跳过
    # 此处pass必须有
    pass


# 定义一个对象
mingy = Student()

# 在定义一个类,用来描述Python的学生


class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

# 需要注意
# 1. def 的缩进层级
    def doHomeWork(self):
        print("我在做作业")

    # 推荐在函数末尾使用return语句
        return None


# 实例化  一个叫yue的学生,是一个具体的人
yue = PythonStudent()
print(yue.name)
print(yue.age)
# 注意成员函数的调用没有
# 传递进入参数
yue.doHomeWork()

print(PythonStudent.__dict__)
print(yue.__dict__)


class Person():
    # name 是共有的成员
    name = "liu"
    # __age就是私有成员
    __age = 18


p = Person()
# name 是公有变量
print(p.name)
# __age是私有变量
# # 注意报错信息
# print(p.__age)
print(Person.__dict__)
print(p._Person__age)