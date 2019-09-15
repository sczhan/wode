
"""
用logging 四大组件来实现日志功能
用装饰器
不同日志, 要记录不同的日志消息
"""

import logging

logger = logging.getLogger("mylogger")
logging.basicConfig(level=logging.DEBUG)

# handler
# TimeRotationFileHandler 是按照日期去划分日志
# RotationFileHandler 是按照日志文件的大小划分日志

debug_handle = logging.FileHandler("1024debug.log")
debug_handle.setLevel(logging.DEBUG)
debug_handle.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

error_handle = logging.FileHandler("1024error.log")
error_handle.setLevel(logging.ERROR)
error_handle.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(debug_handle)
logger.addHandler(error_handle)


def log(f):
    def wraper(*args, **kwargs):
        logger.debug("this is a debug info")
        logger.error("this is a error info")
        return f(*args, **kwargs)
    return wraper

# 按照函数的不同要在日志中打印不同的东西
def loghigher(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.debug(text)
            logger.error(text)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log

def text():
    print("test done")

@loghigher("this is main done")
def main():
    print("main done")

@loghigher("this  is text1 done")
def text1():
    print("text1 done")


if __name__ == '__main__':
    main()
    text1()
    text()


"""
一般情况我们在实际的工作当中, 我们经常把logging封装成一个装饰器, 
按照自己习惯, 新建一个loggerTools的文件,在需要保存日志的地方, 把loggerTool给引进来
"""

