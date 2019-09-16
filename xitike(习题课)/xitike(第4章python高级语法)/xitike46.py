#
# """
# logging.debug
# logging.info
# logging.warning
# logging.error
# logging.critical
# """
# import logging
#
# log_format = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=log_format, filename="my.log")
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.critical("this is critical")



# """
# 装饰器
#  - 使用装饰器,打印函数执行的时间
# """
# import logging
# log_format = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(format=log_format)
# def log(func):
#     def wrapper(*arg, **kw):
#         logging.error(" this is info message")
#         return func(*arg, **kw)
#     return wrapper
# @log
# def test():
#     print("test done")
# @log
# def main():
#     print("main does")
# test()
# main()


"""
使用装饰器, 根据不同函数,传入不同日志
"""
import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format)


def log(tex):
    def decorator(func):
        def wapper(*arg, **kw):
            logging.error(tex)
            return func(*arg, **kw)
        return wapper
    return decorator

@log("test done")

def test():
    print("test done")

@log("main done")
def main():
    print("main done")

test()
main()