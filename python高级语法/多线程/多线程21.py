
import os
from multiprocessing import Process


def info(title):
    """
    :param title:
    :return:
    """
    print(title)
    print("module name", __name__)
    # 得到父亲进程的id
    print("parent process", os.getppid())
    # 得到本身进程的id
    print(("parent id", os.getpid()))


def f(name):
    """
    :param name:
    :return:
    """
    info("function f")
    print("hell ", name)


if __name__ == "__main__":
    info("main line")
    p = Process(target=f, args=("bob",))
    p.start()
    p.join()