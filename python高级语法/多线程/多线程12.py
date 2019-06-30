
import threading
import time

sum = 0
loopSum = 10000000

lock = threading.Lock()


def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁, 申请锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()


def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁, 申请锁
        lock.acquire()
        sum -= 1
        # 释放锁
        lock.release()


if __name__ == "__main__":
    print("Start   ... {0}".format(sum), time.ctime())
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("End ... {0}".format(sum), time.ctime())

