# class Student():
#     name = "dana"
#     age = 18
#
#
# # 实例化
# yue = Student()
# print(Student.__dict__)
# print(yue.__dict__)


# class A():
#     name = "dana"
#     age = 18
#
#     # 注意函数的写法,参数有一个self
#     def say(self):
#         self.name = "aaaa"
#         self.age = 200


# # 此时,A成为类实例
# print(A.name)
# print(A.age)
#
# print("*"*20)
#
# # id可以鉴别一个变量是否和另一个变量是同一变量
# print(id(A.name))
# print(id(A.age))
#
#
# print("*"*20)
# a = A()
# print(A.__dict__)
# print(a.__dict__)
# print(a.name)
# print(a.age)
# print(id(a.name))
# print(id(a.age))
#
# # 此案例说明
# # 类实例的属性和其对象实例的属性在不对对象的实例属性赋值的前提下,指向同一个变量
# # 修改对象的实例属性
# a.name = "liu"
# a.age = 15
# print(a.__dict__)
# print(a.name)
# print(a.age)
# print(id(a.name))
# print(id(a.age))

# class Student():
#     name = "da"
#     age = 18
#
#     #注意say的写法,参数有一个self
#     def say(self):
#         self.name = "aaaa"
#         self.age = 200
#         print("my name is {0}".format(self.name))
#         print("my age is {0}".format(self.age))
#
#     def sayAgain(s):
#         s.name = "aaaa"
#         s.age = 200
#         print("my name is {0}".format(s.name))
#         print("my age is {0}".format(s.age))
#
#
# yue = Student()
# yue.say()
# yue.sayAgain()

#
# class Tercher():
#     name = "55"
#     age = 19
#
#     def say(self):
#         self.name = "aaaa"
#         self.age = 200
#         print("my name is {0}".format(self.name))
#         print("my age is {0}".format(__class__.age))
#
#     def sayAgain():
#         print("again ")
#         print("my name is {0}".format(__class__.name))
#
#
# t = Tercher()
# t.say()
# # 调用  绑定类函数实用类名
# Tercher.sayAgain()
# print(t.__class__.name)


# 关于self的案列
class A():
    name = "pp"
    age = 20

    def __init__(self):
        self.name = "kkkk"
        self.age = 240

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = "bbb"
    age = 18


a = A()
# 此时,系统会默认把a作为第一个参数传入函数
a.say()
# 此时self被a替代
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 此时,传入的是类实例B,因为B具有name 和 age 属性,所以不会报错
A.say(B)

# 以上代码,利用鸭子模型


class Person():
    # name 是共有的成员
    name = "liu"
    # __age就是私有成员
    __age = 18


p = Person()
print(p.name)
# __age是私有变量,注意报错信息
# print(p.__age)
print(Person.__dict__)
print(p._Person__age)




