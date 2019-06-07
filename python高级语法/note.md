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
    
    
   
    
    