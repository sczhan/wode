

"""
利用time函数, 生成两个函数
顺序调用
计算总运行时间
"""
import _thread as thread
import time


def loop1():
    """
    :return:
    """
    # ctime 得到当前时间
    # print("Start loop1 at: {0}".format(time.ctime()))
    print("Start loop1 at: ", time.ctime())
    # 睡眠多长时间, 单位是秒
    time.sleep(4)
    print("End loop1 at: ", time.ctime())


def loop2():
    """
    :return:
    """
    # ctime 得到当前时间
    print("Start loop2 at: ", time.ctime())
    # 睡眠多长时间, 单位是秒
    time.sleep(2)
    print("End loop2 at: ", time.ctime())


def main():
    """
    :return:
    """
    print("Starting at: ", time.ctime())
    # 启动多线程的意思是有多线程去执行某个函数
    # 启动多线程函数为 start_new_thread
    # 参数两个, 一个是需要运行的函数名, 第二是函数的参数作为元组使用,为空则使用空元组
    # 注意: 如果函数只有一个参数,需要参数后有一个逗号
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    # print("All done at: ", time.ctime())


if __name__ == "__main__":
    main()
    # while True:
    #     time.sleep(7)


    time.sleep(7)
    print("All done at: ", time.ctime())

