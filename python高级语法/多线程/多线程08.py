
import threading
import time


def loop1():
    """
    :return:
    """
    print("Start loop 1 at:   ", time.ctime())
    time.sleep(6)
    print("End loop 1 at:  ", time.ctime())


def loop2():
    """
    :return:
    """
    print("Start loop 2 at:   ", time.ctime())
    time.sleep(2)
    print("End loop 2 at:  ", time.ctime())


def loop3():
    """
    :return:
    """
    print("Start loop 3 at:   ", time.ctime())
    time.sleep(5)
    print("End loop 3 at:  ", time.ctime())


def main():
    """
    :return:
    """
    print("Start at:   ",time.ctime())
    # 生成Threading.Thread 实例
    t1 = threading.Thread(target=loop1, args=())
    # setName 是给每一个子线程设置一个名字
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    # setName 是给每一个子线程设置一个名字
    t2.setName("THR_2")
    t2.start()
    # t2.join()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName("THR_3")
    t3.start()
    # t3.join()

    # 预期3秒后, thread2 已经自动启动
    time.sleep(3)
    # enumerate 得到正在运行的子线程, 即子线程1和子线程3
    for thr in threading.enumerate():
        # getName能够得到线程的名字
        print("正在运行的线程名字是:  {0}".format(thr.getName()))
    print("正在运行的子线程数量为:   {0}".format(threading.activeCount()))
    print("All done at:   ", time.ctime())


if __name__ == "__main__":
    main()