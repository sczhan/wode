
"""
使用多线程去播放两个列表, 一个是movie, 一个是music
 - thread
 - threading
"""
import _thread as thread
import time

movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁.rmvb", "xxx.mp4"]
mosic_list = ["周杰伦.mp3", "五月天.mp3"]
movie_format = ["mp4", "avi", "rmvb"]
mosic_format = ["mp3"]


def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("你现在收看的是:{}".format(i))
            time.sleep(3)
        elif i.split(".")[1] in mosic_format:
            print("你现在收听的是:{}".format(i))
            time.sleep(2)
        else:
            print("没有播放格式")


def thread_run():
    thread.start_new_thread(play, (movie_list,))
    thread.start_new_thread(play, (mosic_list,))
    # while True:
    #     time.sleep(10)


if __name__ == "__main__":
    thread_run()


# import threading
# import time
#
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁.rmvb", "xxx.mp4"]
# mosic_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ["mp4", "avi", "rmvb"]
# mosic_format = ["mp3"]
#
#
# def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("你现在收看的是:{}".format(i))
#             time.sleep(3)
#         elif i.split(".")[1] in mosic_format:
#             print("你现在收听的是:{}".format(i))
#             time.sleep(2)
#         else:
#             print("没有播放格式")
#
#
# def thread_run():
#     t1 = threading.Thread(target=play, args=(mosic_list,))
#     t2 = threading.Thread(target=play, args=(movie_list,))
#     t1.start()
#     t2.start()
#
#
# if __name__ == "__main__":
#     thread_run()