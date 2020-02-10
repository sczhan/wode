# 属性案例
# 创建Student类,描述学生类
# 学生具有Student.name属性
# 但name格式不统一


# class Student():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # 如果不想修改代码
#         self.setName(name)
#
#     # 介绍一下自己
#     def intro(self):
#         print("my name is {0}".format(self.name))
#         print("my age is {0}".format(self.age))
#
#     def setName(self, name):
#         self.name = name.upper()
#
#
# s1 = Student("liuying", 19)
# s2 = Student("michi stangle", 24)
# s2.intro()
# s1.intro()
#
#
# # property案例
# # 定义一个Person类,具有name, age属性
# # 对于任意输入的姓名,我们希望都用大写的方式保存
# # 对于年龄,我们希望内部统一用整数保存
# # x = property(fget, fset, fdel, doc)
class Person():
    """
    这是一个人,一个高尚的人
    他还有属性
    """
    # 函数名称可以任意
    def fget(self):
        return self.name*2

    def fset(self, name):
        # 所有输入的姓名以大写形式保存
        self.name = name.upper()

    def fdel(self):
        self.name = "noname"

    name1 = property(fget, fset, fdel, "对name进行操作")


p = Person()
p.name1 = "tuling"
print(p.name1)
print("*" * 20)
#
#
# # 类的内置函数举例
# print(Person.__dict__)
# print(Person.__doc__)
# print(Person.__bases__)
# print(Person.__name__)
# print(Person.__dir__)
#
#
#
# # 构造函数 init举例
# class A():
#     def __init__(self):
#         print("哈哈,我被调用了")
#
#
# a = A()
#
#
# # __call__举例
# class A():
#     def __init__(self):
#         print("哈哈,我被调用了")
#
#     def __call__(self):
#         print("我被调用")
#
#
#
# a = A()
# a()
#
#
# # __str__举例
# class A():
#     def __init__(self):
#         print("哈哈,我被调用了")
#
#     def __call__(self):
#         print("我被调用")
#
#     def __str__(self):
#         print("字符串")
#
#
# a = A()
# a()
# print(a)

# # __getattr__
# class A():
#     name = "noname"
#     age = 18
#
#     def __getattr__(self, name):
#         print("没找到")
#         print(name)
#
#
# a = A()
# print(a.name)
# print(a.addr)
#
#
# # __setattr__案例
# class Person():
#     def __init__(self):
#         pass
#     def __setattr__(self, name, value):
#         print("设置属性:{0}".format(name))
#         # 下面语句会导致问题,死循环
#         # self.name = value
#         # 此种情况,为了避免死循环,规定统一父类魔法函数
#         super().__setattr__(name, value)
#
# p = Person()
# print(p.__dict__)
# p.age = 18
#
#
# # __gt__
# class Student():
#     def __init__(self, name):
#         self._name = name
#
#     def __gt__(self, obj):
#         print("哈哈哈,{0} 会比{1}大吗".format(self, obj))
#         return self._name > obj._name
#
#
# stu1 = Student("one")
# stu2 =Student("two")
# print(stu1 > stu2)


# 三种方法的案例
class Person:
    # 实例方法
    def eat(self):
        print(self)
        print("eat..")

    # 类方法
    # 类方法的第一个参数,一般命名为cls, 区别去self
    @classmethod
    def paly(cls):
        print(cls)
        print("play...")

    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("say...")


p = Person()
# 实例方法
p.eat()
# 类方法
Person.paly()
p.paly()
# 静态方法
p.say()
Person.say()

# # 变量的三种用法
#
# class A():
#     def __init__(self):
#         self.name = "hahha"
#         self.age = 18
#
#
# a = A()
# # 属性的三种用法
# # 1 赋值
# # 2 读取
# # 3 删除
# a.name = "LIU"  # 赋值
# print(a.name)  # 读取
# del a.name   # 删除
# # print(a.name) 删除后会报错
#
#
# # 类属性 property
# # 应用场景:
# # 对变量除了普通的三中操作,还想增加一些附加的操作,那么可以通过property完成
#
# class A():
#     def __init__(self):
#         self.name = "hahha"
#         self.age = 18
#
#     # 此功能,是对类变量进行读取操作的时候应该执行的函数功能
#     def fget(self):
#         print("我被读取了")
#         return self.name
#
#     # 模拟的是对变量进行写操作的时候执行的功能呢
#     def fset(self, name):
#         print("我被写入了")
#         self.name = "图灵学院:" + name
#
#     # 模拟的是删除变量的时候进行操作
#     def fdel(self):
#         print("我别删除")
#
#     # property的四个参数顺序是固定的
#     # 第一个参数代表读取的时候需要调用的函数
#     # 第二个参数代表写入的时候需要调用的函数
#     # 第三个是删除
#     name2 = property(fget, fset, fdel, "这是一个property的例子")
#
#
# a = A()
# print(a.name)
# print(a.name2)
# a.fset("ll")
# print(a.name2)
