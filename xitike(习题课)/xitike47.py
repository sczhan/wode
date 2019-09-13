
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
@log


def text():
    print("test done")

text()