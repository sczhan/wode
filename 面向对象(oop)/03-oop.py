
# # 继承的语法
# # 在python中,任何类都有一个共同的父类叫 object
# class Person():
#     name = "None name"
#     age = 0
#     _petname = "sec"  # 小名  是保护的, 子类可以用,但不能公用
#     __score = 0  # 考试成绩是秘密,只能自己知道
#
#     def sleep(self):
#         print("Sleeping...........")
#
#
# # 父类写在括号内
# class Teacher(Person):
#     teacher_id = "9527"
#
#     def make_test(self):
#         print("attention")
#
#
# t = Teacher()
# print(t.name)
# # 受保护不能外部访问,为啥这里可以
# print(t._petname)
# # 私有访问问题
# # 公开访问私有变量,报错
# # print(t.__score)
# t.sleep()
# t.make_test()
# print(t.teacher_id)


# # 子类和父类定义同一个名称变量,则优先使用子类本身
#
#
# class Person():
#     name = "None name"
#     age = 0
#     _petname = "sec"  # 小名  是保护的, 子类可以用,但不能公用
#     __score = 0  # 考试成绩是秘密,只能自己知道
#
#     def sleep(self):
#         print("Sleeping...........")
#
#
# # 父类写在括号内
# class Teacher(Person):
#     teacher_id = "9527"
#     name = "liu"
#
#     def make_test(self):
#         print("attention")
#
#
# t = Teacher()
# print(t.name)


# # 子类扩充父类功能的案列
# class Person():
#     name = "None name"
#     age = 0
#     _petname = "sec"  # 小名  是保护的, 子类可以用,但不能公用
#     __score = 0  # 考试成绩是秘密,只能自己知道
#
#     def sleep(self):
#         print("Sleeping...........")
#
#     def work(self):
#         print("make some money")
#
#
# # 父类写在括号内
# class Teacher(Person):
#     teacher_id = "9527"
#     name = "liu"
#
#     def make_test(self):
#         print("attention")
#
#     def work(self):
#         # 扩充父类的功能只需要调用父类相应的函数
#         # Person.work(self)
#         # 扩充父类的另一种方法
#         # super代表得到父类
#         super().work()
#         self.make_test()
#
#
# t = Teacher()
# t.work()


# # 构造函数的概念
# class Dog():
#     # __init__就是构造函数
#     # 每次实例化的时候,第一个被自动调用
#     # 因为主要工作是进行初始化,所有得名
#     def __init__(self):
#         print("l am dog")
#
#
# # 实例化的时候,括号内的参数需要跟构造函数匹配
# kaka = Dog()


# # 继承中的构造函数
# class Animel():
#     def __init__(self):
#         print("animel")
#
#
# class PaxingAni(Animel):
#     def __init__(self):
#         print("爬行动物")
#
#
# class Dog(PaxingAni):
#     # __init__就是构造函数
#     # 每次实例化的时候,第一个被自动调用
#     # 因为主要工作是进行初始化,所有得名
#     def __init__(self):
#         print("l am dog")
#
#
# # 实例化的时候,自动调用了Dog构造函数
# # 因为找到了构造函数,则不再查找父类的构造函数
# kaka = Dog()
#
# # 猫没写构造函数
#
#
# class Cat(PaxingAni):
#     pass
#
#
# # 此时应该自动调用构造函数,应为Cat没有构造函数,所以查找父类构造函数
# # 在PaxingAni中查找到了构造函数,则停止向上查找
# c = Cat()


# # 继承中的构造函数 -2
class Animel():
    def __init__(self):
        print("animel")


class PaxingAni(Animel):
    def __init__(self, name):
        print("爬行动物{0}".format(name))
#
#
# class Dog(PaxingAni):
#     # __init__就是构造函数
#     # 每次实例化的时候,第一个被自动调用
#     # 因为主要工作是进行初始化,所有得名
#     def __init__(self):
#         print("l am dog")
#
#
# # 实例化Dog时,查找到Dog的构造函数,参数匹配,不报错
# d = Dog()
#
#
class Cat(PaxingAni):
    pass

#
# # 此时,由于Cat没有构造函数,则向上查找
# # 因为PaxingAni的构造函数需要两个参数,实例化的时候给了一个,报错
c = Cat("ok")
print("*" * 20)


# 继承中的构造函数 -3
class Animel():
    def __init__(self):
        print("animel")


class PaxingAni(Animel):
        pass


class Dog(PaxingAni):
    pass



# 实例化Dog时,查找到Dog的构造函数,参数匹配,不报错
d = Dog()



class Cat(PaxingAni):
    pass


# 此时,由于Cay没有构造函数,则向上查找
# 因为PaxingAni的构造函数需要两个参数,实例化的时候给了一个,报错
c = Cat()

print(type(super))
