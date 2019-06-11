# 1 模块
-  一个模块就是一个包含python代码的文件,后缀名是.py就可以,模块就是个python文件
- 为什么我们用模块
    - 程序太大,编写维护非常不方便,需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用,避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件,所以任何代码可以直接书写
    - 不过根据模块的规范,最好在模块中编写以下内容
        - 函数 (单一功能)
        - 类 (相似功能的组合,或者类似业务模块)
        - 测试代码
- 如何使用模块
    - 模块直接导入
        - 加入模块名称直接以数字开头,需要借助importlib帮助
    - 语法
        import module_name 
        module_name.function_name
        module_name.class_name
        - 案例 01, 02, p01, p02
    
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法跟第一种相同
        - 案列 p03
    
    - from module_name import func_name, class_name
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容,不需要前缀
        - 案列 p04
    
    - from module_name import *
        - 导入模块所有内容
        - 案列 p05 
    
- if __name__ == "__main__":的使用
    - 可以有效避免模块代码被导入的时候别动执行的问题
    - 建议所有程序的入口都以此代码为入口
   

# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径
    - 加载模块的时候,系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
    
    import sys
    sys.path  属性可以获取路径列表
    案列 p06
- 添加搜索路径
        sys.path.append(dir)
- 模块加载顺序
    1. 搜索内存中已经加载好的模块
    2. 搜索python内置模块
    3. 搜索sys.path路径


# 包
- 包是一种组织管理代码的方式,包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构
        | - - - 包
        | - - - | - - - __init__.py  包的标志文件
        | - - - | - - - 模块1
        | - - - | - - - 模块2
        | - - - | - - - 子包(子文件夹)
        | - - - | - - - | - - - __init__.py  包的标志文件
        | - - - | - - - | - - - 子包模块1
        | - - - | - - - | - - - 子包模块2
        
- 包的导入操作
     - import package_name
     - 直接导入一个包,可以使用 __init__.py 中的内容
     - 使用方式:
            package_name.func_name
            package_name.class_name.func_name()
    - 此种方式的访问内容是
    - 案列 pck01, p07
    
    - import package_name as p
        - 具体用法跟作用方式,跟上述简单导入一致
        - 注意的是此种方法默认对__init__.py内容的导入
    
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
            package.module.func_name
            package.module.class.fun()
            package.module.class.var
        - 案列 p08
        
    - import package.module as pm
    
- from ...  import 导入
    - from package import module1, module2, module3, ....
    - 此种导入方法不执行__init__ 的内容
            
            from pck01 import p01
            p01.sayhello()
    
    - from package import *
        - 导入当前包 "__init__.py"文件中所有的函数和类
        - 使用方法
                func_name()
                class_name.func_name()
                class_name.var
        - 案列 p09  注意此种导入的具体内容
        
- from package.module import *
    - 导入包中指定的模块的所有内容
    - 使用方法
            func_name()
            class_name.func_name()
            
- 在开发环境中经常会使用其他模块,可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块路径 

- "__all__"方法
    - 在使用from package import *  的时候, * 可以导入的内容
    - "__init__.py"中如果文件为空, 或者没有"__all__", 那么只可以把__init__中的内容导入
    - "__init__" 如果设置了 "__all__" 的值,那么则按照 "__all__",指定的子包或者模块进行加载,
    如此不会载入 "__init__" 中的内容
    - "__all__=["module1", "module2", "package", ...]
    - 案列 pck02, p10
    

# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突
        setName()
        Student.setName()
        Dog.setName()


# 异常
##jupyter notebook 异常处理.ipynb
 - 广义上次错误分为错误和异常
 - 错误指的是可以人为避免
 - 异常是指语法逻辑正确运行的前提下,出现的问题
 - 在python里,异常是一个类,可以处理和使用

# 异常的分类
    AssertError 断言语句（assert）失败
    AttributeError 尝试访问未知的对象属性
    EOFError 用户输入文件未尾标志EOF（Ctrl+d）
    FloatingPointError 浮点计算错误
    GeneratorExit generator.close（）方法被调用的时候
    ImportError 导入模块失败的时候
    IndexError 索引超出序列的范围
    KeyError 字典中查找一个不存在的关键字
    KeyboardInterrupt，用户输入中断键（Ctrl+c）
    MemoryError 内存溢出（可通过删除对象释放内存）
    NameError尝试访问一个不存在的变量
    NotImplementedError 尚未实现的方法
    0SError 操作系统产生的异常（例如打开一个不存在的文件）
    0verflowError 数值运算超出最大限制
    ReferenceError 弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
    RuntimeError 一般的运行时错误
    StopIteration 迭代器没有更多的值
    SyntaxError Python的语法错误
    IndentationError 缩进错误
    TabError Tab和空格混合使用
    SystemError Python编译器系统错误
    SystemExit Python编译器进程被关闭
    TypeError 不同类型间的无效操作
    UnboundLocalError 访问一个未初始化的本地变量（NameError的子类）
    UnicodeError Unicode相关的错误（ValueError的子类）
    UnicodeEncodeError Unicode编码时的错误（UnicodeError的子类）
    UnicodeDecodeError Unicode解码时的错误（UnicodeError的子类）
    UnicodeTranslateError Unicode转换时的错误（UnicodeError的子类）
    ValueError 传入无效的参数
    ZeroDivisionError 除数为零

l = [1, 2, 3, 4, 5, "liudana"]
print(l[5])
    
print(100/12)
# 常常犯的除零错误
num = int(input("请输入数字:"))
print(100/num)



# 异常处理
 - 不能保证程序永远正确运行
 - 但是必须保证程序在最坏的情况下得到的问题被妥善处理
 - python 的异常处理模块全部语法为:
        try:
            尝试实现某个操作，
            如果没出现异常，任务就可以完成
            如果出现异常，将异常从当前代码块扔出去尝试解决异常
        except异常类型1：
            解决方案1：用于尝试在此处处理异常解决问题
        except 异常类型2：
            解决方案2：用于尝试在此处处理异常解决问题
        except（异常类型1，异常类型2...）
            解决方案：针对多个异常使用相同的处理方式
        excpet：
            解决方案：所有异常的解决方案
        else：
            如果没有出现任何异常，将会执行此处代码
        finally：
            管你有没有异常都要执行的代码

- 流程
    1. 执行try下面的语句
    2. 如果出现异常,则在except语句中查找对应异常并进行处理
    3. 如果没有出现异常,则执行else语句内容
    4. 最后,不管是否出现异常,都要执行finally语句
- 除except(最少一个)以外,else和finally可选
# 简单异常案列
try:
    num = int(input("请输入数字:"))
    rst = 100 / num
    print("计算结果是:{0}".format(rst))
except:
    print("你特娘的输入的啥玩意")
    # 程序退出
    exit()

# 简单异常案列
# 给出提示信息
try:
    num = int(input("请输入数字:"))
    rst = 100 / num
    print("计算结果是:{0}".format(rst))
# 捕获异常后,把异常实例化,出错信息在实例里
# 注意以下写法
# 以下语句是捕获ZeroDivisionError异常并实例化e
except ZeroDivisionError as e:
    print("你特娘的输入的啥玩意")
    print(e)
    # 程序退出
    exit()# 
# 作业: 为什么我们可以直接打印出实例e,此时实例e应该实现了那个函数

# 简单异常案列
# 给出提示信息
try:
    num = int(input("请输入数字:"))
    rst = 100 / num
    print("计算结果是:{0}".format(rst))
# 如果是多种error的情况
# 需要把具体的错误,越往前放
# 在异常类继承关系中,越是子类的异常,越要往前放
# 越是父亲类的异常,越要往后放 

# 处理异常的时候,一旦拦截到某一个异常,则不在继续往下查,直接进行下一个代码, 
# 有finally则执行finally语句块,否则就执行下一个大的语句

except ZeroDivisionError as e:
    print("你特娘的输入的啥玩意")
    print(e)
    # 程序退出
    exit()# 
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("好像属性有问题")
    print("e")
    exit()
    
# 所有异常都是继承自Exception
# 如果写上下面这句话,任何异常都会拦截
# 而且,下面这句话一定是最后一个excetion
except Exception as e:
    print("我也不知道就出错了")
    print(e)
print("hhh")     

   
# 用户手动引发异常
 - 当某些情况,用户希望自己引发一个异常的时候,可以使用
 - raise 关键字引发异常
      
# raise 案例
try:
    print("我爱刘梦")
    print(1314)
    # 手动引发一个异常
    # 注意语法: raise ErrorClassName
    raise NameError
    print("还没完呀")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我会被执行")    


# raise 案例2
# 自己定义异常
# 需要注意:  自定义异常必须是系统异常的子类
class DanaValueError(ValueError):
    pass
try:
    print("我爱刘梦")
    print(1314)
    # 手动引发一个异常
    # 注意语法: raise ErrorClassName
    raise DanaValueError
    print("还没完呀")
except NameError as e:
    print("NameError")
# except DanaError as e:
#     print("DanaError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我会被执行")
    

# esle 语句案例

try:
    print("l love liumeng")
    num = int(input("请输入数字:"))
    rst = 100 / num
    print("计算结果是:{0}".format(rst))
except Exception as e:
    print("Exception")
else:
    print("No Exception")
finally:
    print("反正我会被执行")

# 关于自定义异常
 - 只要是raise异常,则推荐自定义异常
 - 在自定义异常的时候,一般包含以下内容:
     - 自定义发生异常的异常代码
     - 自定义发生异常后的问题提示
     - 自定义发生异常的行数
 - 最终的目的是,一旦发生异常,方便程序员快速定位错误现场
    


# 常用模块
##jupyter notebook 常用模块.ipynb
 - calendar
 - time
 - datetime
 - timeit
 - os
 - shutil
 - zip
 - math
 - string
 - 上述所有模块使用理论上都应该先导入,string是特例
 - calendar, time, datetime的区别参考中文意思   

#calendar
 - 跟日历相关的模块

# 使用需要先导入
import calendar

# calendar: 获取一年的日历字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2019)
print(cal)
print(type(cal))  

# isleap:判断某一年是否闰年
calendar.isleap(2004)

# leapdays: 获取指定年份之间的闰年的个数
calendar.leapdays(2001, 2018)

# month() 获取某个月的日历字符串
# 格式: calendar.month(年,月)
# 回值:月日历的字符串
m3 = calendar.month(2019, 3)
print(m3)

# monthrange() 获取一个月的周几开始即和天数
# 格式: calendar.monthrange(年, 月)
# 回值: 元组(周几开始, 总天数)
# 注意: 周默认0-6表示周一到周天
help(calendar.monthrange)
t = calendar.monthrange(2019, 6)
print(t)
w, t = calendar.monthrange(2019, 6)
print(w)
print(t)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式: calendar.monthcalendar(年, 月)
# 回值: 二级矩阵
# 注意: 矩阵中没有天数用0表示
m = calendar.monthcalendar(2019, 6)
print(type(m))
print(m)

# prcal: print calendar 直接打印日历
calendar.prcal(2019)
help(calendar.prcal)

# prmonth()  直接打印整个月的日历
# 格式: calendar.prmonth(年, 月)
# 返回值:无
calendar.prmonth(2019, 6)

# weekday()  获取周几
# 格式: calendar.weekday(年, 月, 日)
# 返回值: 周几对应的数字
calendar.weekday(2019, 6, 26)


# time模块
### 时间戳
   - 一个时间表示,根据不同语言,可以是整数或者浮点数
   - 是从1970年1月1日0时0分0秒到现在经历的秒数
   - 如果表示的时间是1970年以前或者太遥远的未来, 可能出现异常
   - 32位操作系统能够支持到2038年
### UTC时间
    - UTC 又称为时间协调时间, 以英国的格尼治天文所在地区的时间作为参考,也叫做世界标准时间
    - 中国时间是 UTC+8 东八区

### 夏令时
    - 夏令时就是夏天的时候将时间调快一小时,本意是督促大家早睡早起节省蜡烛! 每天变成25小时,本质没变还是24小时
    
### 时间元组
    - 一个包含时间内容的普通元组
    
    索引   内容    属性        值
    0     年      tm year     2015
    1     月      tm mon      1~12
    2     日      tm mday     1~31
    3     时      tm hour     0～23
    4     分      tm min      0～59
    5     秒      tm sec      0~61  60表示闰秒   61保留值
    6     周几     tm wday     0~6
    7     第几天    tm yday     1~366
    8     夏令时    tm_isdst    0，1，-1（表示夏令时）

# 需要单独导入
import time

# 时间模块的属性
# timezone: 当前时区的UTC时间相差的描述,在没有夏令时的情况下的间隔,东八区的是 -28800
# altzone: 获取当前时区与UTc时间相差的秒数,在有夏令时的情况下
# daylight: 检测当前是否是夏令时时间状态, 0 表示是

print(time.timezone)
print(time.daylight)

# 得到时间截
time.time()

# localtime 得到当前时间的时间结构
# 可以通过点号操作符得到当前的
t = time.localtime()
print(t)
print(t.tm_hour) 
print(type(t))

# asctime() 返回元组的正常字符串化之后的时间格式
# 格式: time.asctime(时间元组)
# 返回值: 字符串Tue Jun 6 11:11:00 2017
t = time.localtime()
print(t)
tt = time.asctime(t)
print(type(tt))
print(tt)

# ctime: 获取字符串化的当前时间
t = time.ctime()
print(type(t))
print(t)

# mktime()  使用时间元组获取对应的时间戳
# 格式: time.mktime(时间元组)
# 返回值: 浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)

# clock: 获取cpu时间 3.0 - 3.3 版本直接使用, 3.6使用有问题
def p():
    time.sleep(2.5)

t0 = time.clock()
p()
# time.sleep(3)
t1 = time.clock()
print(t0, t1)
print(t1 - t0)

# sleep: 使程序进入睡眠,n秒后继续
for i in range(10):
    print(i)
    time.sleep(1)
    
# strftime: 将时间元组转化为自定义的字符串格式
"""
    格式  含义

    %a   本地简化星期名称
    %A   本地完整星期名称
    %b   本地简化的月份名称
    %B   本地完整的月份名称
    %c   本地相应的日期表示和时间表示
    %d   月内中的一天（0-31）
    %j   年内的一天（001-366）
    %m   月份（01-12）
    %M   分钟数（00=59）
    %p   本地A.M.或P.M.的等价符
    %S   秒（00-59）
    %U   一年中的星期数（00-53）星期天为星期的开始
    %w   星期（0-6），星期天为星期的开始
    %W   一年中的星期数（00-53）星期一为星期的开始
    %x   本地相应的日期表示
    %X   本地相应的时间表示
    %y   两位数的年份表示（00-99）
    %Y   四位数的年份表示（000-9999）
    %Z   当前时区的名称
    %%   %号本身

"""
# 把时间表示成 2019年6月9日 16:09
t = time.localtime()
ft = time.strftime("%Y{0}%m{1}%d{2} %H:%M",  t).format("年", "月", "日")
print(ft)


# datetime模块
- datetime 提供日期和时间的运算和表示

import datetime
# datetime 常见属性
# datetime.date: 一个理想的日期,提供year,month,day属性
print(datetime.date(2019, 6, 9))
dt = datetime.date(2019, 6, 9)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.time: 提供一个理想和的时间,提供hour, minute, sec, microsec 等内容
# datetime.datetime: 提供日期跟时间的组合
# datetime.timedelta:提供一个时间差,时间长度

# datetime.datetime
from datetime import datetime
# 常用类方法
# today:
# now
# utcnow
# fromtimestamp: 从时间戳中返回本地时间
dt = datetime(2019, 6, 9)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta
# 表示一个时间间隔
from datetime import datetime, timedelta
t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m-%d %H:%M:%S"))

# td表示1小时10分钟的时间长度
td = timedelta(hours=1,minutes=10)
# 当前时间加上时间间隔后,把得到的一个小时10分钟后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))


# timeit: 时间测量工具

# 测量程序运行时间间隔实验
def p():
    time.sleep(3.6)

t1 = time.time()
p()
print(time.time() - t1)


# 生成列表两张方法比较
# 如果单纯比较生成一个列表的时间,可能很难实现
import timeit
c = """
sum = []
for i in range(1000):
    sum.append(i)
"""

# 利用timeit调用代码,执行100000次,查看运行时间
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)

# timeit 可以执行一个函数,来测量一个函数的执行时间
def dolt():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))

# 执行函数 打印10次
t = timeit.timeit(stmt=dolt, number=10)
print(t)


s = """ 
def dolt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
"""

# 执行dolt(num)
# setup负责把环境变量准备好
# 实际相当于给timeit创造了一个小环境
# 在创作的小环境中, 代码执行的顺序大致是
# 
"""def dolt(num):
        ...
num = 3
dolt(num)
"""
t = timeit.timeit("dolt(num)", setup=s+"num=3", number=10)
print(t)


# datetime.datetime 模块
- 提供比较好用的时间而已
- 类定义
    class datetime. datetime(year, month, dayI, hour
    [, minute
    [, second
    [, microsecond
    [, tzinfo]]]]])
# The year, month and day arguments are required.
    MINYEAR <=year <=MAXYEAR
    1<=month <=12
    1<=day<=n
    0<=hour<24
    0<=minute<60
    0<=second<60
    0<=microsecond<10**6
- 类方法
- datetime.today（）：返回当前本地datetime.随着tzinfo None.这个等同于
- datetime.fromtimestamp（time.time（））.
- datetime.now（[tz]）：返回当前本地日期和时间，如果可选参数tz为None或没有详细说明，这个方法会像today（）.
- datetime.utcnow（）：返回当前的UTC日期和时间，如果tzinfo None，那么与now（）类似。
- datetime.fromtimestamp（timestamp[，tz]）：根据时间戳返回本地的日期和时间.tz指定时区
- datetime.utcfromtimestamp（timestamp）：根据时间戳返回 UTC datetime.
- datetime.fromordina（ordinal）：根据Gregorian ordinal 返回datetime.
- datetime.combine（date，time）：根据date和time返回一个新的datetime.
- datetime.strptime（date string，format）：根据date string和format返回一个datetime.
- 实例方法
- datetime.date（）：返回相同年月日的date对象，
- datetime.time（）：返回相同时分秒微秒的time对象。
- datetime.replace（kw）：kw in[year，month，day，hour，minute，second，microsecond，tzinfo]，与date类似.
- datetime.min:datetime（MINYEAR，1，1）.datetime.max:datetime（MAXYEAR，12，31，23，59，59，999999）.
- 实例属性（read-only）
- datetime.year：1至9999 datetime.month：1至12 datetime.day：1至n datetime.hour:In range（24）.0至23 datetime.minute:In range（60）.datetime.second:In range（60）.
- datetime.microsecond:In range（1000000）


# os - 操作系统相关
- 跟操作系统相关, 主要是文件操作
- 与系统相关的操作, 主要包含在三个模块里
    - os, 操作系统目录相关
    - os.path, 系统路径相关操作
    - shutil, 高级文件操作, 目录树的操作,文件赋值,删除,移动
- 路径:
    - 绝对路径: 总是从根目录上开始
    - 相对路径: 基本以当前环境为开始的一个相对的对方
    
# os 模块
# getcwd() 获取当前的工作目录
# 格式: os.getcwd()
# 返回值: 当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作,默认查找文件的目录
import os
mydir = os.getcwd()
print(mydir)


# chdir() 改变当前的工作目录
# change directory
# 格式: os.chdir(路径)
# 返回值: 无
os.chdir("/home/sczhan")
mydir = os.getcwd()
print(mydir)


# listdir() 获取一个目录中所有子目录和文件的名称列表
# 格式: os.listdir(路径)
# 返回值:所有子目录和文件名称的列表
ld = os.listdir("D:\未来教育")
print(ld)
ld = os.listdir()
print(ld)


# makedirs() 递归创建文件夹
# 格式: os.makedirs(递归路径)
# 返回值: 无
# 递归路径: 多个文件夹层次包含的路径就是递归路径, 例如a/b/c..
rst = os.makedirs("D:\战")
print(rst)

# system()  运行系统shell命令
# 格式: os.system(系统命令)
# 返回值: 打开一个shell或者终端界面
# ls是列出当前文件和文件夹的系统命令
# 一般推荐使用subprocess代替
# windows是dir  linux是ls
rst = os.system("dir")
print(rst)

# window 还不知道 下面是linux
# 在当前目录下创建一个dana.haha 的文集
rst = os.system("touch zhan.txt")
print(rst)

# getenv() 获取指定的系统环境变量值
# 相应的还有putenv
# 格式:  os.getenc("环境变量")
# 返回值: 指定环境变量名对应的值
rst = os.getenv("PATH")
print(rst)

# exit()   退出当前程序
# 格式: exit()
# 返回值: 无

# 值部分
- os.curdir: curretn dir 当前目录
- os.pardir: parent dir 父亲目录
- os.sep: 当前系统的路径分隔符
    - windows: "\"
    - linux: "/"
- os.linesep: 当前系统的换行符号
    - windows:  "\r\n"
    - unix,linux,macos: "\n"
- os.name: 当前系统名称 
    - windows: nt
    - mac, unix, linux: posix
    

print(os.name)
print(os.curdir)
print(os.pardir)
print(os.sep) 

# 在路径相关操作中, 不要手动拼写地址,因为手动拼写的路径可能不具有移值性
path = "/home/tlxy" + "/" + "dana"
print(path)



# os.path模块, 跟路径相关的模块

# abspath()  将路径转化为决定路径
# abselute 绝对
#格式: os.path.abspath("路径")
# 返回值: 路径的绝对路径形式

# linux 中
# . 点,代表当前目录
# .. 双点, 代表父目录
import os.path as op
absp = op.abspath(".")
print(absp)

# basename() 获取路径中的文件名部分
# 格式: os.path.basename(路径)
# 返回值:  文件名字符串
bn = op.basename("Users")
print(bn)
bn = op.basename("Users\SCzha")
print(bn)

# join() 将多个路径合成一个路径
# 格式:  os.path.join(路径1, 路径2,...)
# 返回值: 组合之后的新路径字符串
bd = "D:\迅雷下载"
fn = "[迅雷下载www.2tu.cc]一路向西.BD1280超清国粤双语中字.txt"
p = op.join(bd, fn)
print(p)

# split() 将路径切割为文件夹部分和当前文件部分
# 格式: os.path.split(路径)
# 返回值: 路径和文件名组成的元组

t = op.split("D:\迅雷下载\[迅雷下载www.2tu.cc]一路向西.BD1280超清国粤双语中字.txt")
print(t)
d, p = op.split("D:\迅雷下载\[迅雷下载www.2tu.cc]一路向西.BD1280超清国粤双语中字.txt")
print(d, p)

# isdir()  检查是否是目录
# 格式: os.path.isdir(路径)
# 返回值; 布尔值
rst = op.isdir("D:\迅雷下载\[迅雷下载www.2tu.cc]一路向西.BD1280超清国粤双语中字.txt")
print(rst)
rst = op.isdir("D:\迅雷下载")
print(rst)

# exists()  检测文件或者目录是否存在
# 格式: os.path.exists(路径)
# 返回值: 布尔值
e = op.exists("D:\迅雷下载")
print(e)
e = op.exists("D:\迅雷下载\ll")
print(e)



# shutil 模块

# copy() 复制文件
# 格式:  shutil.copy(来源路径, 目标路径)
# 返回值: 返回目标路径
# 拷贝的同时, 可以给文件重命名
import shutil
rst = shutil.copy("D:\迅雷下载\[迅雷下载www.2tu.cc]一路向西.BD1280超清国粤双语中字.txt"
                 ,"D:\迅雷下载\[迅雷下载www.2tu.cc]一路向西.txt")
print(rst)

# copy2()  复制文件, 保留元数据
# 格式:  shutil.copy2(来源路径, 目标路径)
# 返回值: 返回目标路径
# 注意: copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据

# copyfile() 讲一个文件中的内容复制到另一个文件当中
# 格式: shutil.copyfile("原路径", "目标路径")
# 返回值: 无
rst = shutil.copyfile("D:\迅雷下载\[迅雷下载www.2tu.cc]一路向西.txt", 
                      "D:\迅雷下载\D迅雷下载[迅雷下载www.2tu.cc]一路向西.BD1280.txt")
print(rst)

# move() 移动文件/ 文件夹
# 格式: shutil.move(原路径, 目标路径)
# 返回值: 目标路径
rst =  shutil.move("D:\迅雷下载\[迅雷下载www.2tu.cc]一路向西.BD1280.txt", 
                   "D")
print(rst)


# 归档和压缩
- 归档: 把对个文件或者文件夹合并到一个文件当中
- 压缩: 用算法把多个文件或者文件夹无损或者有损合并到一个文件当中

# make_archive() 归档操作
# 格式: shutil.make_archive("归档之后的目录文件名", "后缀", "需要归档的文件夹")
# 返回值: 归档之后的地址
import os
# 是想得到一个叫做 战.me 的归档文件
rst = shutil.make_archive("D:\迅雷下载\zhan", "zip", "D:\迅雷下载\jjjkk")
print(rst)

# unpack_archive()  解包操作
# 格式: shutil.unpack_archive("归档文件地址", "解包之后的地址")
# 返回值: None

rst = shutil.unpack_archive("D:\迅雷下载\zhan.zip", "D:\迅雷下载\jjjkkkk")
print(rst)


# zip-压缩包
- 模块名称叫 zipfile

# zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# 创建一个ZipFile对象,表示一个zip文件.参数file表示文件的路径或类文件对象(file-like object);参数
import zipfile as zf
zf = zf.ZipFile("D:\迅雷下载\zhan.zip")

# ZipFile.getinfo(name):
# 获取zip文档内指定文件的信息. 返回一个zipfile.ZipInfo对象, 它包括文件的详细信息
rst = zf.getinfo("[迅雷下载www.2tu.cc]一路向西.txt")
print(rst)

# ZipFile.namelist()
# 获取zip文档内所有文件的名称列表

nl = zf.namelist()
print(nl)

# ZipFile.extractall([path[, menbers[, pwd]]])
# 解压zip文档中的所有文件到当前目录.

rst = zf.extractall("D:\迅雷下载\zhan")
print(rst)


# random
- 随机数
- 所有随机模块都是伪随机

# random() 获取0-1之间的随你小数
# 格式: random.random()
# 返回值: 随机0-1之间的小数
import random 
print(random.random())

# choice() 随机返回序列中的某个值
# 格式: ramdom.choice(序列)
# 返回值: 序列中的某个值
l = [str(i)+ "haha" for i in range(10)]
rst = random.choice(l)
print(rst)

# shuffle()  随机打乱列表
# 格式: random.shuffle(列表)
# 返回值:打乱顺序之后的列表
l1 = [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)

# random.randint(a, b): 返回一个a到b之间的随机整数,包含a和b
print(random.randint(0, 100))


# Log模块资料
- https://www.cnblogs.com/yyds/p/6901864.htmL 


# Python语言的高级特性
## 函数式编程(FunctionProgramming)
- 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数, 同样可以作为返回值
    - 纯函数编程语言: LISP, Haskell
- Python函数式编程只是借鉴函数式编程的一些特点,可以理解成一半函数式一半Python
- 需要讲述
    - 高阶函数
    - 返回函数
    - 匿名函数
    - 装饰器
    - 偏函数
    

### lambda表达式
- 函数: 最大程序复用代码
    - 存在问题: 如果函数很小, 很短, 则会造成啰嗦
    - 如果函数调用次数很少,则会造成浪费
    - 对应阅读者来说,造成阅读流程的被迫中断
- lambda表达式(匿名函数):
    - 一个表达式,函数体相对简单
    - 不是一个代码块, 仅仅是一个表达式
    - 可以与参数,有很多个参数也可以,用逗号隔开


# "小" 函数举例
def printA():
    print("aaaa")
printA()

# lambda表达式的用法
# 1 以lambda开头
# 2 紧跟一定的参数(如果有的话)
# 3 参数后用冒号和表达式主题隔开
# 4 只是一个表达式, 所有,没有return

# 计算一个数字的100倍数
# 因为就是一个表达式,所以没有return
stm = lambda x: 100 * x
print(stm(89))
# 使用上跟函数调用一模一样
stm(89)


stm2 = lambda x, y, z: x + y + z * 100
print(stm2(1, 2, 3))
stm2(1, 2, 3)