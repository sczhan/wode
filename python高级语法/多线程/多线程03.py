
import _thread as thread
import time


def loop1(inl):
    """
    :param inl:
    :return:
    """
    # ctime得到当前时间
    print("Start loop 1 at: ", time.ctime())
    # 把参数打印出来
    print("我是参数: ", inl)
    # 睡眠多长时间,单位是秒
    time.sleep(4)
    print("End loop 1 at:  ", time.ctime())


def loop2(inl, in2):
    """
    :param inl:
    :param in2:
    :return:
    """
    # ctime得到当前时间
    print("Start loop 1 at: ", time.ctime())
    # 把参数打印出来
    print("我是参数: ", inl, "和参数2: ", in2)
    # 睡眠多长时间,单位是秒
    time.sleep(4)
    print("End loop 1 at:  ", time.ctime())


def main():
    """
    :return:
    """
    print("Starting at: ", time.ctime())
    # 启动多线程的意思是有多线程去执行某个函数
    # 启动多线程函数为 start_new_thread
    # 参数两个, 一个是需要运行的函数名, 第二是函数的参数作为元组使用,为空则使用空元组
    # 注意: 如果函数只有一个参数,需要参数后有一个逗号
    thread.start_new_thread(loop1, ("wyz", ))
    thread.start_new_thread(loop2, ("love", "lm"))


if __name__ == "__main__":
    main()
    time.sleep(7)
    print("All done at: ", time.ctime())
