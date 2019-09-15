
"""
用协程的方式完成播报
"""
# import asyncio
# import time
#
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁.rmvb"]
# mosic_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ["mp4", "avi",]
# mosic_format = ["mp3"]
#
#
# @asyncio.coroutine
# def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("now playing movie named {}".format(i))
#             yield time.sleep(3)
#         elif i.split(".")[1] in mosic_format:
#             print("now playing music named {}".format(i))
#             yield time.sleep(2)
#         else:
#             print("no playing")
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     task = [play(movie_list), play(mosic_list)]
#     loop.run_until_complete(asyncio.wait(task))
#     loop.close()

# async await
# import asyncio
# import time
# import multiprocessing
#
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁.rmvb"]
# mosic_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ["mp4", "avi", ]
# mosic_format = ["mp3"]
#
#
# async def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("now playing movie named {}".format(i))
#             await asyncio.sleep(3)
#         elif i.split(".")[1] in mosic_format:
#             print("now playing music named {}".format(i))
#             await asyncio.sleep(2)
#         else:
#             print("no playing")
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     task = [play(movie_list), play(mosic_list)]
#     loop.run_until_complete(asyncio.wait(task))
#     loop.close()

"""
使用协程的概念, 达到以下概念, 输入 a,b,c,d 四个整数, 打印出(a+b)*(c+d)的值
假设 a+b 和 c+d 是一个耗时 1S 的IO操作
"""
import asyncio
import threading
import time


async def sum(a, b):
    print("现在开始准备计算{0}{1}".format(threading.currentThread(), time.ctime()))
    r = int(a) + int(b)
    await asyncio.sleep(1)
    print("现在计算完了, current {0}{1}".format(threading.currentThread(), time.ctime()))
    return r

loop = asyncio.get_event_loop()
task = asyncio.gather(sum(1, 2), sum(3, 4))
loop.run_until_complete(task)
r1, r2 = task.result()
print(int(r1) * int(r2))
loop.close()

"""
常用  多进程 + 协程的方式
"""