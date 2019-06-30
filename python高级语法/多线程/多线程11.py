
import threading
import time

sum = 0
loopSum = 100000000


def myAdd():
    """
    :return:
    """
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1


def myMinu():
    """
    :return:
    """
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1


# print(time.ctime())
# myAdd()
# print(sum)
# myMinu()
# print(sum)
# print(time.ctime())


if __name__ == "__main__":
    print("Start   ... {0}".format(sum), time.ctime())
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("End ... {0}".format(sum), time.ctime())