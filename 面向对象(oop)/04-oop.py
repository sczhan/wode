#
# # class A():
# #     pass
# #
# # class B(A):
# #     pass
# #
# #
# # class C(B,A):
# #     pass
# #
# # print(A.__mro__ )
# # print(B.__mro__ )
# # print(C.__mro__ )
#
# #  多继承案列
# # 子类可以直接拥有父类的属性和方法,私有属性和方法除外(保护,私有的)
#
# class Fish():
#     def __init__(self, name):
#         self.name = name
#
#     def swim(self):
#         print("swimming")
#
#
# class Bird():
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("flying")
#
#
# class Person():
#     def __init__(self, name):
#         self.name = name
#
#     def worked(self):
#         print("working")
#
#
# # 单继承的列子
# class Student(Person):
#     def __init__(self, name):
#         self.name = name
#
#
# stu = Student("yue")
# stu.worked()
#
#
# # 多继承的例子
# class SuperMan(Person, Bird, Fish):
#     def __init__(self, name):
#         self.name = name
#
#
# s = SuperMan("ll")
# s.fly()
# s.swim()
#
#
# # 菱形问题代码
# class A():
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(B, C):
#     pass


# # 构造函数例子
# class Person():
#     # 对Person类进行实例化的时候
#     # 姓名要确定
#     # 年龄得确定
#     # 地址肯定有
#     def __init__(self):
#         self.name = "NoName"
#         self.age = 18
#         self.address = "Studentwhonheim"
#         print("in init func")
#
#
# # 实例化一个人
# p = Person()
#
#
# # 构造函数的调用顺序 -1
# # 如果子类没有写构造函数,则自动向上查找,直到找到位置
#
# class A():
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#
#
# class C(B):
#     pass
#
#
# # 此时,首先查找C的构造函数
# # 如果没有则向上按照MRO顺序查找父类的构造函数,直到找到为止
# c = C()


# # 构造函数的调用顺序 -2
# class A():
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self, name):
#         print(name)
#         print("B")
#
#
# class C(B):
#     pass
#
#
# # 此时,首先查找C的构造函数
# # 如果没有则向上按照MRO顺序查找父类的构造函数,直到找到为止
# # 此时,会出现参数结构不对应错误
# # c = C()
# c = C("55")   # 参数结构对应,不报错


# # 构造函数的调用顺序 -3
# class A():
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self, name):
#         print("B")
#         print(name)
#
#
# class C(B):
#     # C中想扩展B的构造函数
#     # 即调用B构造函数后添加一些功能
#     # 有两种方法实现
#     # 第一种是通过父类名调用
#     '''
#     def __init__(self, name):
#         # 首先调用父类的构造函数
#         B.__init__(self, name)
#         # 其次,在增加自己的功能
#         print("C附加的功能")
#     '''
#
#     # 第二种,使用super调用
#     def __init__(self, name):
#         super(C, self).__init__(name)  # super().__init__(name)
#         print("这是C附加")
#
#
# c = C("我是C")


# Mixin案例
class Person():
    name = "liuying"
    age = 18

    def eat(self):
        print("eat...")


    def  drink(self):
        print("drink...")


    def sleep(self):
        print("sleep...")


class Teacher(Person):
    def work(self):
        print("work")


class Student(Person):
    def stu(self):
        print("study")


class Tutor(Teacher, Student):
    pass


t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)
print(Person.__dict__)
print(Teacher.__dict__)


# Mixin 实现

class TeacherMixin():
    def work(self):
        print("work")


class StudengMixin():
    def stu(self):
        print("study")


class TutorMixin(Person, TeacherMixin, StudengMixin):
    pass


print("*"*20)
tt = Tutor()
tt.stu()
tt.work()
print(TutorMixin.__mro__)
print(tt.__dict__)
print(TutorMixin.__dict__)
print(Person.__dict__)
print(TeacherMixin.__dict__)



# # issubclass
# class A():
#     pass
#
#
# class B(A):
#     pass
#
#
# class C():
#     pass
#
#
# print(issubclass(B,A))
# print(issubclass(C,A))
# print(issubclass(B,object))
#
#
# # isinstance
# class A():
#     pass
#
#
# a = A()
# print(isinstance(a,A))
# print(isinstance(A,A))


# # hasattr
# class a():
#     name = "no"
#
#
# A = a()
# print(hasattr(A, "name"))
# print(hasattr(A, "AGE"))
#
#
# # dir案例
#
# class A():
#     pass
#
#
# a = A()
# print(dir(A))
# print(dir(a))
