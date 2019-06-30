
import threading
import time


def func():
    """
    :return:
    """
    print("l am running ....")
    time.sleep(4)
    print("l am done ......")


if __name__ == "__main__":
    t1 = threading.Timer(6, func)
    t1.start()

    i = 0
    while True:
        print("{0}............".format(i))
        time.sleep(3)
        i += 1