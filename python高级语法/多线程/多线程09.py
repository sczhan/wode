
import threading
import time


# 1.类实例需要继承threading.Thread
class MyThread(threading.Thread):
    """
    类实例需要继承threading.Thread
    """
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 2. 必须重写润还是, run函数代表的是真正执行的功能
    def run(self):
        """
        :return:
        """
        time.sleep(2)
        print("The args for is {0}".format(self.arg))


for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()
print("Main thread is done !!!")