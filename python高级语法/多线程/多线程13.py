
import queue
import threading
import time


# Python 2
# from Queue import Queue

# Python 3
# import queue


class Producer(threading.Thread):
    """
    生产者
    """
    def run(self):
        global queue
        count = 0
        while True:
            # qsize 返回queue 内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "生成产品" + str(count)
                    # put 是往queue
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    """
    消费者
    """
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # get 是从queue中取出值
                    msg = self.name + "消费了" + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == "__main__":
    queue = queue.Queue()
    for i in range(500):
        queue.put("初始产品" + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
