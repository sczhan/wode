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


# 抽象
#
# class Ainmel():
#
#     def sayHello(self):
#         pass
#
#
# class Dog(Ainmel):
#     def sayHello(self):
#         print("闻一闻")
#
#
# class Person(Ainmel):
#     def sayHello(self):
#         print("kiss me")
#
#
# d = Dog()
# d.sayHello()
# p = Person()
# p.sayHello()
#
#
# # 抽象类的实现
#
# import abc
# # 声明一个类并且指定当前类的元类
# class Human(metaclass=abc.ABCMeta):
#
#     # 定义一个抽象方法
#     @abc.abstractmethod
#     def smoking(self):
#         pass
#
#     # 定义类抽象方法
#     @abc.abstractclassmethod
#     def drink():
#         pass
#
#     # 定义静态抽象方法
#     @abc.abstractstaticmethod
#     def play():
#         pass
#
#     def sleep(self):
#         print("sleep...")
#
#
# # 自组装一个类
# class A():
#     pass
#
#
# def say(self):
#     print("say..")
#
#
# class B():
#     def say(self):
#         print("saying...")
#
#
# say("a")
# A.say = say
# a = A()
# a.say()
# # a = A()
# # say(a)
# b = B()
# b.say()
#
#
# # 函数名可以当变量使用
# def sayHello(name):
#     print("{0}你好, 来一发吗".format((name)))
#
#
# sayHello("ll")
# liumang = sayHello
# liumang("ll")
#
#
# # 组装类例子 2
# # 自组装一个类
# from types import MethodType
#
#
# class A():
#     pass
#
#
# def say(self):
#     print("say..")
#
#
# class B():
#     def say(self):
#         print("saying...")
#
#
# a = A()
# a.say = MethodType(say,A)
# a.say()


# 利用type造一个类

def say(self):
    print("say....type")


def talk(self):
    print("Talking.....type")


# 利用type来创建一个类
A = type("Aname", (object, ), {"class_say":say, "class_talk":talk})
# 然后可以像正常方法访问一样使用类
a = A()
print(dir(a))
a.class_say()


# 元类演示

# 元类写法是固定的,它必须继承子type
# 元类一般命名以MetaClass结尾
class TilingMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 自己业务处理
        print("我是元类")
        attrs["id"] = "0000"
        attrs["addr"] = "北京市"
        return type.__new__(cls, name, bases, attrs)


class Teather(object, metaclass=TilingMetaClass):
    pass


t = Teather()
print(t.__dict__)
t.id

