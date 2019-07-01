
import multiprocessing
from time import sleep, ctime


class ClockProcess(multiprocessing.Process):
    """
    派生子类
    两个函数比较重要
    1. init 构造函数
    2. run 函数
    """
    def __init__(self, interval):
        super(ClockProcess, self).__init__()
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % ctime())
            sleep(self.interval)


if __name__ == "__main__":
    p = ClockProcess(3)
    p.start()
