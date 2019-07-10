


import multiprocessing
from time import ctime


def consumer(input_q):
    """
    :param input_q:
    :return:
    """
    print("Into consumer: ", ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q") # 此处替代所有有用的工作
    print("Out of consumer", ctime())
    # 此句末执行, 因为q.join()收集到四个task_done()信号后, 主进程启动, 未等到print此句话


def producer(sequence, output_q):
    """
    :param sequence:
    :param output_q:
    :return:
    """
    print("Into procuder: ", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into of q")
    print("Out of procuder: ", ctime())


if __name__ == "__main__":
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p1 = multiprocessing.Process(target=consumer, args=(q, ))
    cons_p1.start()
    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()

    # 生成多个项, sequence 代表要发送给消费者的项序列
    # 在实践中, 这可能是生成器的输出或通过一些其他方式生产出来

    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()