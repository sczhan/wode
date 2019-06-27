import threading
import time


def fun():
    """
    :return:
    """
    print("Start fun")
    time.sleep(2)
    print("End fun")


print("Main thread")
t1 = threading.Thread(target=fun, args=())
t1.start()
time.sleep(1)
print("Main thread end")